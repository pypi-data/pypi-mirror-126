resource "aws_network_interface" "test" {
  count = contains(local.resourcelist, "eni") ? 1 : 0

  subnet_id       = var.subnet_id

  tags = {
      Department = var.tag_value
  }
}