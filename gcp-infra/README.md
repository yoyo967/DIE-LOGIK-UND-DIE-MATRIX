# GCP Infrastructure Provisioning

This directory contains the Terraform configuration files to provision the Google Cloud Platform (GCP) resources for the **INFINITY OS / UNIVERSE M.E.** runtime.

## Provisioned Resources

1.  **Google Cloud Storage (GCS) Bucket:** `gs://universe-me-infinity-raw-data` (Element 1: Raw Intake)
2.  **BigQuery Dataset & Table:** `chronik.traces` (Element 4: Chronik Ledger, Partitioned by Day, Clustered by conversation/agent)
3.  **Firestore Database:** Native default instance (Element 5: State & Loop Session metadata)
4.  **Vertex AI Search (Discovery Engine):** Wiki search engine and generic layout-aware data store (Element 2: Wiki)
5.  **Secret Manager Secrets:** GitHub access token and agent SSH keys bindings.

## How to Deploy

### Prerequisites

1.  Ensure you have the Google Cloud CLI (`gcloud`) installed.
2.  Authenticate with your GCP Account:
    ```bash
    gcloud auth login
    gcloud auth application-default login
    ```
3.  Create or verify your GCP Project: `universe-me-infinity`.
4.  Install Terraform CLI (>= 1.5.0).

### Deployment Steps

1.  Initialize the Terraform workspace:
    ```bash
    terraform init
    ```

2.  Perform a dry-run execution plan:
    ```bash
    terraform plan -var="project_id=universe-me-infinity"
    ```

3.  Apply the configuration to deploy the infrastructure:
    ```bash
    terraform apply -var="project_id=universe-me-infinity"
    ```

4.  Review the output values to configure the local execution bridge.
