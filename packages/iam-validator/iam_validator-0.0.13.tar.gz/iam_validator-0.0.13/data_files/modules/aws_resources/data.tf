data "aws_ami" "amazon-linux" {
    most_recent = true
    owners = ["137112412989"]
    filter  {
        name = "name"
        values = ["amzn2-ami-hvm-2.0.20211005.0-x86_64-gp2"]
    }
}