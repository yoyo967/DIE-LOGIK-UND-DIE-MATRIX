import os
import re
import sys
import subprocess
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Interface INFINITY — Local Bridge Daemon (opus-flow)",
    description="Secure execution bridge between Google Cloud Antigravity and the local filesystem.",
    version="1.1.0"
)

#=============================================================================
# CONFIGURATION & SANDBOX BOUNDARIES
#=============================================================================
# Standard FLOW_ROOT defined in the system specification (BRAIN.md)
DEFAULT_FLOW_ROOT = r"D:\dev\universe-infinity-os"
FLOW_ROOT = Path(os.getenv("FLOW_ROOT", DEFAULT_FLOW_ROOT)).resolve()

print(f"[opus-flow] Initializing with FLOW_ROOT: {FLOW_ROOT}")

# Create FLOW_ROOT directory if it doesn't exist to prevent immediate crash
FLOW_ROOT.mkdir(parents=True, exist_ok=True)

#=============================================================================
# SECURITY ENGINE & REDACTION FILTER
#=============================================================================
FORBIDDEN_PATTERNS = [
    r"\.\.",                         # Directory Traversal
    r"^[a-zA-Z]:(?!\\dev\\universe-infinity-os)", # Rejects absolute paths outside flow root
    r"format-volume",               # Disk formatting
    r"remove-item\s+-recurse",       # Destructive deletions
    r"\bdel\b",                      # Command prompt delete
    r"\brmdir\b",                    # Directory removal
    r"\breg\b",                      # Registry operations
    r"set-executionpolicy",          # Execution policy bypass
    r"\bnetsh\b",                    # Network shell modifications
    r"\bipconfig\b",                 # Network configuration reads
    r"\bnet\b",                      # Network user control
    r"\bicacls\b",                   # Windows ACL modifications
    r"\bchmod\b",                    # Linux permission modifications
    r"\bchown\b"                     # Linux owner modifications
]

SECRET_PATTERNS = [
    r"ghp_[a-zA-Z0-9]{36}",          # GitHub Personal Access Token
    r"github_pat_[a-zA-Z0-9_]{82}",  # GitHub Fine-grained Access Token
    r"-----BEGIN [A-Z ]+ PRIVATE KEY-----[\s\S]+?-----END [A-Z ]+ PRIVATE KEY-----", # Private SSH keys
    r"AIzaSy[a-zA-Z0-9-_]{33}",      # Google API Keys
    r"ey[a-zA-Z0-9-_=]+\.ey[a-zA-Z0-9-_=]+\.[a-zA-Z0-9-_=]+" # JWT tokens
]

def validate_command(command: str) -> bool:
    """
    Validates a PowerShell command against whitelist guidelines and blacklist patterns.
    """
    cmd_lower = command.lower()
    
    # 1. Blacklist check
    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, cmd_lower):
            return False
            
    # 2. Check for absolute path violations (e.g. C:\Windows or C:\Users\...)
    # Matches letters followed by colon and backslash (like C:\)
    all_absolute_paths = re.findall(r"([a-zA-Z]:\\[^\s\"']*)", command)
    for path_str in all_absolute_paths:
        try:
            resolved_path = Path(path_str).resolve()
            if not resolved_path.is_relative_to(FLOW_ROOT):
                return False
        except Exception:
            return False # Invalid path format
            
    return True

def redact_secrets(text: str) -> str:
    """
    Filters out sensitive access tokens, credentials, and keys from terminal output.
    """
    redacted_text = text
    for pattern in SECRET_PATTERNS:
        redacted_text = re.sub(pattern, "[REDACTED_SECRET]", redacted_text, flags=re.IGNORECASE)
    return redacted_text

#=============================================================================
# API MODEL REPRESENTATIONS
#=============================================================================
class PowerShellRequest(BaseModel):
    command: str = Field(..., description="The exact PowerShell command to execute.")

class PowerShellResponse(BaseModel):
    stdout: str = Field(..., description="The standard output captured from execution.")
    stderr: str = Field(..., description="The standard error captured from execution.")
    exitCode: int = Field(..., description="The exit code of the execution.")

class CommitPushRequest(BaseModel):
    repoPath: str = Field(..., description="The absolute local path to the Git repository.")
    commitMessage: str = Field(..., description="The commit message according to system rules.")

class CommitPushResponse(BaseModel):
    commitHash: str = Field(..., description="The SHA-256 commit hash generated.")
    pushSuccess: bool = Field(..., description="True if push succeeded.")

#=============================================================================
# ENDPOINT IMPLEMENTATIONS
#=============================================================================
@app.post("/execute-powershell", response_model=PowerShellResponse)
async def execute_powershell(req: PowerShellRequest):
    """
    Executes a controlled PowerShell command inside the FLOW_ROOT sandbox.
    """
    if not validate_command(req.command):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Command violates system safety guidelines (FLOW_ROOT sandbox escape or forbidden execution pattern)."
        )

    # Resolve execution shell (prefers PowerShell 7 Core 'pwsh', falls back to Windows 'powershell')
    shell_executable = "pwsh"
    try:
        subprocess.run([shell_executable, "-Command", "exit 0"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        shell_executable = "powershell.exe"

    try:
        # Run PowerShell command inside FLOW_ROOT working directory
        result = subprocess.run(
            [shell_executable, "-NoProfile", "-NonInteractive", "-Command", req.command],
            cwd=FLOW_ROOT,
            capture_output=True,
            text=True,
            timeout=60 # Prevent infinite hanging operations
        )
        
        # Redact secrets before returning output
        clean_stdout = redact_secrets(result.stdout or "")
        clean_stderr = redact_secrets(result.stderr or "")
        
        return PowerShellResponse(
            stdout=clean_stdout,
            stderr=clean_stderr,
            exitCode=result.returncode
        )
    except subprocess.TimeoutExpired:
        raise HTTPException(
            status_code=status.HTTP_408_REQUEST_TIMEOUT,
            detail="Powershell command execution timed out after 60 seconds."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Daemon execution failure: {str(e)}"
        )

@app.post("/git-commit-push", response_model=CommitPushResponse)
async def git_commit_push(req: CommitPushRequest):
    """
    Performs safe Git staging, committing, and pushing for audited changes.
    """
    # 1. Path validation to verify repoPath is inside FLOW_ROOT
    try:
        target_repo = Path(req.repoPath).resolve()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid repository path format."
        )
        
    if not target_repo.is_relative_to(FLOW_ROOT):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Git repository must be located within FLOW_ROOT."
        )
        
    if not (target_repo / ".git").exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Repository not found: Path does not contain a .git directory."
        )

    # 2. Execution of staging, committing and pushing
    try:
        # Git Add
        add_result = subprocess.run(
            ["git", "add", "-A"],
            cwd=target_repo, capture_output=True, text=True, check=True
        )
        
        # Git Commit
        commit_result = subprocess.run(
            ["git", "commit", "-m", req.commitMessage],
            cwd=target_repo, capture_output=True, text=True
        )
        
        # Git Push
        push_result = subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=target_repo, capture_output=True, text=True
        )
        
        push_success = (push_result.returncode == 0)
        
        # Retrieve Commit Hash
        hash_result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=target_repo, capture_output=True, text=True, check=True
        )
        
        commit_hash = hash_result.stdout.strip()
        
        if not push_success:
            # Check stderr for common remote rejection issues
            clean_push_err = redact_secrets(push_result.stderr or "")
            return CommitPushResponse(
                commitHash=commit_hash,
                pushSuccess=False
            )
            
        return CommitPushResponse(
            commitHash=commit_hash,
            pushSuccess=True
        )
    except subprocess.CalledProcessError as err:
        clean_err = redact_secrets(err.stderr or err.stdout or str(err))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Git command failed: {clean_err}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error during commit operation: {str(e)}"
        )
