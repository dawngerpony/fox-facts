terraform {
  required_version = "~> 0.13"
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}
