### Terraform Variable precedence

1. Variables passed via command line (-var option or via file -var-file <filename>)
    terraform apply -var='image_id_list=["ami-abc123","ami-def456"]' -var="instance_type=t2.micro"
    or
    terraform apply -var-file="testing.tfvars"
2. Environment variable (TF looks for env vars of the name "TF_VAR_<var name>")
3. Variable's Default value
4. User prompt if there is no default value


Terraform loads variables in the following order, with later sources taking precedence over earlier ones:

    Environment variables
    The terraform.tfvars file, if present.
    The terraform.tfvars.json file, if present.
    Any *.auto.tfvars or *.auto.tfvars.json files, processed in lexical order of their filenames.
    Any -var and -var-file options on the command line, in the order they are provided

https://developer.hashicorp.com/terraform/language/values/variables