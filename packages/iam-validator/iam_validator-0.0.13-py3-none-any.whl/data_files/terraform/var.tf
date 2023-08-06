variable "resources" {
   description = "Comma delimited list of AWS resource names to be created"
   type        = string
   default     = ""
}
variable "tag_value" {
   description = "The tag value for the Request/ResourceTag in the conditional"
   type = string
   default = ""
}

variable "permissions_boundary_arn" {
   description = "Permissions boundary arn"
   type = string
   default = ""
}

variable "aws_region" {
   description = "aws region"
   type = string
   default = "us-east-1"
}

variable "subnet_id" {
    description = "subnet id"
    type = string
    default = ""
}