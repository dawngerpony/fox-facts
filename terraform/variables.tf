variable "credentials" {
  default     = "credentials.json"
  description = "credentials file"
  type        = string
}

variable "project" {
  description = "The name of the GCP project"
  type        = string
}

variable "region" {
  description = "The GCP region"
  type        = string
}

variable "username" {
  description = "Your GCP username"
  type        = string
}

variable "ssh_private_key_filename" {
  default     = "~/.ssh/id_rsa.pub"
  description = "The location of your SSH private key"
  type        = string
}