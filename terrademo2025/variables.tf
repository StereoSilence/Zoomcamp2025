variable "credentials" {
  description = "My credentials"
  default     = "./keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default     = "sixth-beaker-447414-d6"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuerry Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Starage Bucket Name"
  default     = "sixth-beaker-447414-d6-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}