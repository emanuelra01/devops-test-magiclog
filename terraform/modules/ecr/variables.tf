variable "ecr_name" {
  description = "The name of the ECR registry"
  type        = any
  default     = null
}


variable "tags" {
  description = "The key-value maps for tagging"
  type        = map(string)
  default     = {}
}
