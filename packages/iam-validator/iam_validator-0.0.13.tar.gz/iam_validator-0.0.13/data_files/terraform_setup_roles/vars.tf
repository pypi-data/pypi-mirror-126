variable "negative_testing_role_name" {
  description = "negative testing role name"
  type = string
  default = "NegativeTestingRole"
}

variable "positive_testing_role_name" {
  description = "positive testing role name"
  type = string
  default = "PositiveTestingRole"
}

variable "developer_testing_role_name" {
  description = "developer testing role name"
  type = string
  default = "DeveloperTestingRole"
}

variable "account_id" {
  description = "AWS Account ID"
  type = string
}

variable "user_name" {
  description = "AWS username"
  type = string
}

variable "department" {
  description = "Department name"
  type = string
}

variable "aws_region" {
   description = "aws region"
   type = string
}

variable "bucket_name" {
    description = "aws s3 bucket name for terraform state files"
    type = string
}