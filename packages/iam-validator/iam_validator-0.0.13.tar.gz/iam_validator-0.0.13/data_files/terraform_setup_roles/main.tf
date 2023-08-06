

resource aws_iam_policy user_policy {
  name = "iam-validator-assume-role-policy"
  description = "Assume role policy which gets attached to the user"
  policy = templatefile("${path.cwd}/policies/user_assume_role_policy.json",
  {
      account_id =var.account_id
      positivive_testing_role_name = var.positive_testing_role_name
      negative_testing_role_name = var.negative_testing_role_name
  })

}


resource aws_iam_policy developer_terraform_policy{
        name = "developer-terraform-policy"
        description = "Policy to allow developer access to terraform statefile"
        policy = templatefile("${path.cwd}/policies/developer_terraform_policy.json",
        {
                bucket_name = var.bucket_name
        })

}


resource aws_iam_policy permissions_boundary_policy{
        name = "permissions-boundary-policy"
        description = "Permissions boundary"
        policy = templatefile("${path.cwd}/policies/developer_permissions_boundary.json",{})

}

resource aws_iam_policy developer_attached_policy{
        name = "developer-attached-policy"
        description = "Developer attached policy"
        policy = templatefile("${path.cwd}/policies/developer_attached_policy.json",
        {
                account_id = var.account_id
                department = var.department
                aws_region = var.aws_region
        })
}


resource aws_iam_role iam_validator_negative_testing_role {
    name = var.negative_testing_role_name
    description = "Negative testing role"
    path = "/"

    assume_role_policy = templatefile("${path.cwd}/policies/trust-policy.json",
    {
        account_id = var.account_id
        user_name = var.user_name
    })
}


resource aws_iam_role iam_validator_positive_testing_role {
    name = var.positive_testing_role_name
    description = "Positive testing role"
    path = "/"

    assume_role_policy = templatefile("${path.cwd}/policies/trust-policy.json",
    {
        account_id = var.account_id
        user_name = var.user_name
    })
}


resource aws_iam_role iam_validator_developer_testing_role {
    name = var.developer_testing_role_name
    description = "Developer testing role"
    path = "/"
    permissions_boundary = aws_iam_policy.permissions_boundary_policy.arn
    assume_role_policy = templatefile("${path.cwd}/policies/trust-policy.json",
    {
        account_id = var.account_id
        user_name = var.user_name
    })
    tags = {
       Department = var.department
    }
}


resource aws_iam_role_policy_attachment development_policy_attach{
        role = aws_iam_role.iam_validator_developer_testing_role.name
        policy_arn = aws_iam_policy.developer_terraform_policy.arn
}

resource aws_iam_role_policy_attachment read_only_policy_attach {
        role = aws_iam_role.iam_validator_developer_testing_role.name
        policy_arn = "arn:aws:iam::aws:policy/ReadOnlyAccess"
}

resource aws_iam_role_policy_attachment developer_attached_policy{
        role = aws_iam_role.iam_validator_developer_testing_role.name
        policy_arn = aws_iam_policy.developer_attached_policy.arn
}
