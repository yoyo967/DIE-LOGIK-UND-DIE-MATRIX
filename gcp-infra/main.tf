terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

#=============================================================================
# ELEMENT 1: RAW DATA INTAKE (GCS Bucket)
#=============================================================================
resource "google_storage_bucket" "raw_data" {
  name                        = "${var.project_id}-raw-data"
  location                    = var.region
  force_destroy               = true
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    condition {
      age = 90
    }
    action {
      type = "Delete"
    }
  }
}

#=============================================================================
# ELEMENT 4: CHRONIK LEDGER (BigQuery Dataset & Traces Table)
#=============================================================================
resource "google_bigquery_dataset" "chronik" {
  dataset_id                  = "chronik"
  friendly_name               = "Chronik Dataset"
  description                 = "Verschluesselte, unveraenderliche Chronik-Logs von Universe M.E."
  location                    = var.region
  default_table_expiration_ms = null # Unendlich haltbar
}

resource "google_bigquery_table" "traces" {
  dataset_id = google_bigquery_dataset.chronik.dataset_id
  table_id   = "traces"
  project    = var.project_id

  time_partitioning {
    type  = "DAY"
    field = "timestamp"
  }

  clustering = ["conversation_id", "agent_id"]

  schema = <<EOF
[
  {
    "name": "timestamp",
    "type": "TIMESTAMP",
    "mode": "NULLABLE",
    "description": "Zeitpunkt der Ausfuehrung (Default CURRENT_TIMESTAMP)"
  },
  {
    "name": "agent_id",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "Eindeutige ID des ausfuehrenden ACP-Agenten"
  },
  {
    "name": "conversation_id",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "Verknuepfung zur aktuellen Benutzer-Session"
  },
  {
    "name": "playbook_name",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "Aktives Verhaltensmuster"
  },
  {
    "name": "step_description",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "Beschreibung der aktuellen Aktion"
  },
  {
    "name": "reasoning_trace",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "Der vollstaendige Gedankengang der KI (Raw LLM Output)"
  },
  {
    "name": "tool_calls",
    "type": "JSON",
    "mode": "NULLABLE",
    "description": "Liste der aufgerufenen OpenAPI-Tools inkl. Argumente"
  },
  {
    "name": "tool_results",
    "type": "JSON",
    "mode": "NULLABLE",
    "description": "Rueckgabewerte der aufgerufenen Tools (stdout/stderr)"
  },
  {
    "name": "prev_integrity_hash",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "Der Hash des vorherigen Log-Eintrags (Ketten-Anker)"
  },
  {
    "name": "integrity_hash",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "Der eigene Hash: SHA-256(timestamp | agent_id | conversation_id | prev_integrity_hash | reasoning_trace)"
  }
]
EOF
}

#=============================================================================
# ELEMENT 5: STATE & LOOP METADATA (Firestore native)
#=============================================================================
resource "google_firestore_database" "state_db" {
  project     = var.project_id
  name        = "(default)"
  location_id = var.region
  type        = "FIRESTORE_NATIVE"
}

#=============================================================================
# ELEMENT 2: WIKI KNOWLEDGE (Vertex AI Search Data Store)
#=============================================================================
resource "google_discovery_engine_data_store" "wiki_store" {
  project             = var.project_id
  location            = "global"
  data_store_id       = "universe-me-wiki-store"
  display_name        = "Universe ME Wiki Data Store"
  industry_vertical   = "GENERIC"
  content_config      = "CONTENT_REQUIRED"
  solution_types      = ["SOLUTION_TYPE_SEARCH"]
  create_link_pipeline = true
}

resource "google_discovery_engine_search_engine" "wiki_search" {
  project        = var.project_id
  location       = "global"
  engine_id      = "universe-me-wiki-search"
  display_name   = "Universe ME Wiki Search"
  data_store_ids = [google_discovery_engine_data_store.wiki_store.data_store_id]
  search_config {}
}

#=============================================================================
# ACCESS SECURITY: SECRET MANAGER (Secrets Kapselung)
#=============================================================================
resource "google_secret_manager_secret" "github_token" {
  secret_id = "github-access-token"
  project   = var.project_id

  replication {
    auto {}
  }
}

resource "google_secret_manager_secret" "ssh_key" {
  secret_id = "agent-ssh-key"
  project   = var.project_id

  replication {
    auto {}
  }
}
