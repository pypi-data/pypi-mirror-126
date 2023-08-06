
 module "aws_resources" {
   source = "../modules/aws_resources"
   resources = var.resources
   tag_value  = var.tag_value
   permissions_boundary_arn = var.permissions_boundary_arn
   aws_region = var.aws_region
   subnet_id = var.subnet_id

}