resource "aws_ebs_volume" "example" {
  count = contains(local.resourcelist, "ebs") ? 1 : 0

  availability_zone = "${var.aws_region}a"
  size              = 40

  tags = {
    Name = "${var.tag_value}-ebs"
    Department = var.tag_value
  }
}