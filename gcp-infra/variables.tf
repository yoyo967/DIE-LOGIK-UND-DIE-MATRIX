variable "project_id" {
  description = "The GCP Project ID where resources will be deployed."
  type        = string
  default     = "universe-me-infinity"
}

variable "region" {
  description = "The GCP Region for regional resources."
  type        = string
  default     = "europe-west3"
}

variable "zone" {
  description = "The GCP Zone for compute/storage bindings."
  type        = string
  default     = "europe-west3-a"
}
