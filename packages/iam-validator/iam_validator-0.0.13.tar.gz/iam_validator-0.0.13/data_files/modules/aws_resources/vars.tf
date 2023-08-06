variable "aws_region" {
   description = "To set the AWS region"
}

variable "resources" {
   description = "Comma delimited list of AWS resource names to be created"
   type        = string
}
variable "tag_value" {
   description = "The tag value for the Request/ResourceTag in the conditional"
   type = string
}

variable "permissions_boundary_arn" {
   description = "Permissions boundary arn"
   type = string
}

variable "subnet_id" {
    description = "Subnet id"
    type = string
}