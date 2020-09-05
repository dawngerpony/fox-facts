terraform {
  required_version = "~> 0.13"
}

// Configure the Google Cloud provider
provider "google" {
  credentials = file("credentials.json")
}
