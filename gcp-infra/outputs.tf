output "raw_data_bucket_name" {
  description = "The name of the GCS Bucket created for raw data intake."
  value       = google_storage_bucket.raw_data.name
}

output "chronik_dataset_id" {
  description = "The BigQuery Dataset ID created for the Ledger."
  value       = google_bigquery_dataset.chronik.dataset_id
}

output "chronik_table_id" {
  description = "The BigQuery Table ID created for traces."
  value       = google_bigquery_table.traces.table_id
}

output "state_database_name" {
  description = "The name of the Firestore database."
  value       = google_firestore_database.state_db.name
}

output "wiki_data_store_id" {
  description = "The Vertex AI Search Data Store ID."
  value       = google_discovery_engine_data_store.wiki_store.data_store_id
}

output "wiki_search_engine_id" {
  description = "The Vertex AI Search Engine ID."
  value       = google_discovery_engine_search_engine.wiki_search.engine_id
}
