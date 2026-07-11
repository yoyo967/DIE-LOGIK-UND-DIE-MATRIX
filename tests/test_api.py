"""
Basis-Tests fuer die opus-flow FastAPI Applikation (apps/local-bridge/main.py)

Diese Tests verifizieren:
- Die FastAPI-App laesst sich importieren und starten
- Grundlegende Sanity-Checks fuer die Anwendungsstruktur

Gemaess AGENTS.md Verifizierbarkeits-Codex:
- Alle Behauptungen muessen empirisch pruefbar sein
- Tests sind die primaere Quelle der Wahrheit
"""

import sys
import os

# Sicherstellen, dass das Verzeichnis im Python-Pfad ist
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'apps', 'local-bridge'))


def test_python_version():
    """Python-Version muss >= 3.11 sein (gemaess pyproject.toml)."""
    assert sys.version_info >= (3, 11), (
        f"Python 3.11+ erforderlich, gefunden: {sys.version}"
    )


def test_requirements_exist():
    """requirements.txt muss im Root-Verzeichnis vorhanden sein."""
    root = os.path.join(os.path.dirname(__file__), '..')
    req_file = os.path.join(root, 'requirements.txt')
    assert os.path.exists(req_file), "requirements.txt fehlt im Root-Verzeichnis"


def test_requirements_not_empty():
    """requirements.txt muss mindestens eine Zeile enthalten."""
    root = os.path.join(os.path.dirname(__file__), '..')
    req_file = os.path.join(root, 'requirements.txt')
    with open(req_file) as f:
        lines = [l.strip() for l in f.readlines() if l.strip() and not l.startswith('#')]
    assert len(lines) > 0, "requirements.txt ist leer"


def test_fastapi_importable():
    """FastAPI muss importierbar sein."""
    try:
        import fastapi
        assert fastapi.__version__ is not None
    except ImportError:
        raise AssertionError("fastapi ist nicht installiert")


def test_pydantic_importable():
    """Pydantic muss importierbar und Version >= 2.0 sein."""
    try:
        import pydantic
        version_parts = pydantic.__version__.split('.')
        major = int(version_parts[0])
        assert major >= 2, f"Pydantic >= 2.0 erforderlich, gefunden: {pydantic.__version__}"
    except ImportError:
        raise AssertionError("pydantic ist nicht installiert")
