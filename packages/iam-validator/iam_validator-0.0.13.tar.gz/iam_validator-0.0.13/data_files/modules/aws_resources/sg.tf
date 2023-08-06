resource "aws_security_group" "test_sg" {
  count = contains(local.resourcelist, "sg") ? 1 : 0

  name        = "${var.tag_value}-test_sg"
  description = "iam-validator test security group"

  egress {
    description      = "for all outgoing traffics"
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Department = var.tag_value
  }
}