resource "aws_iam_role" "role_w_boundary" {
 count = contains(local.resourcelist, "iam_role") && length(var.permissions_boundary_arn)>0 ? 1 : 0
 name        = "IAM-Validating-Testing-Role"
 description = "IAM Validation Testing Role"
 path = "/${var.tag_value}/"
 assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
  permissions_boundary = var.permissions_boundary_arn
 tags = {
  Department = var.tag_value
 }
}


resource "aws_iam_role" "role_wo_boundary" {
 count = contains(local.resourcelist, "iam_role") && length(var.permissions_boundary_arn)<1 ? 1 : 0
 name        = "IAM-Validating-Testing-Role"
 description = "IAM Validation Testing Role"
 path = "/${var.tag_value}/"
 assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
 tags = {
  Department = var.tag_value
 }
}