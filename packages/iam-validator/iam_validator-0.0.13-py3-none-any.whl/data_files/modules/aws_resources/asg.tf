data "aws_availability_zones" "available" {}

resource "aws_launch_configuration" "lc" {
  count = contains(local.resourcelist, "asg") ? 1 : 0
    name = "${var.tag_value}-lc"
    image_id = data.aws_ami.amazon-linux.id
    instance_type = "t2.micro"
}

resource "aws_autoscaling_group" "asg" {
    count = contains(local.resourcelist, "asg") ? 1 : 0
    name = "${var.tag_value}-asg"
    vpc_zone_identifier = [var.subnet_id]
    launch_configuration = aws_launch_configuration.lc[0].name
    min_size =1
    max_size=1
    force_delete = true
    tag {
        key = "Department"
        value = var.tag_value
        propagate_at_launch = true
    }
}

resource "aws_autoscaling_policy" "asgp" {
    count = contains(local.resourcelist, "asg") ? 1 : 0
    depends_on = [aws_autoscaling_group.asg[0]]
    name = "${var.tag_value}-asgp"
    autoscaling_group_name = "${var.tag_value}-asg"
    adjustment_type = "ChangeInCapacity"
    scaling_adjustment = 1
    cooldown = 600
    policy_type = "SimpleScaling"
}



