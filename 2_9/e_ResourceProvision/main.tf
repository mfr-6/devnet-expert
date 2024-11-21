terraform {
  required_providers {
    aci = {
      source  = "CiscoDevNet/aci"
      version = "0.7.0"
    }
  }
}

provider "aci" {
  username = "admin"
  password = "C1sco12345"
  url      = "https://10.10.20.14"
  insecure = true
}

resource "aci_tenant" "provisioner_tenant1" {
  name = "provisioner_tenant1"
  provisioner "local-exec" {
    command = "echo \"I just configured Tenant: ${self.name} on APIC! ID: ${self.id}\""
  }
}

# Plan: 1 to add, 0 to change, 0 to destroy.
# aci_tenant.provisioner_tenant1: Creating...
# aci_tenant.provisioner_tenant1: Provisioning with 'local-exec'...
# aci_tenant.provisioner_tenant1 (local-exec): Executing: ["/bin/sh" "-c" "echo \"I just configured Tenant: provisioner_tenant1 on APIC! ID: uni/tn-provisioner_tenant1\""]
# aci_tenant.provisioner_tenant1 (local-exec): I just configured Tenant: provisioner_tenant1 on APIC! ID: uni/tn-provisioner_tenant1
# aci_tenant.provisioner_tenant1: Creation complete after 2s [id=uni/tn-provisioner_tenant1]

resource "aci_tenant" "provisioner_tenant2" {
  name = "provisioner_tenant2"
  provisioner "remote-exec" {
    connection {
      type     = "ssh"
      host     = "10.10.20.14"
      user     = "admin"
      password = "C1sco12345"
    }

    inline = ["show tenant"]
  }
}

# aci_tenant.provisioner_tenant2: Creating...
# aci_tenant.provisioner_tenant2: Provisioning with 'remote-exec'...
# aci_tenant.provisioner_tenant2 (remote-exec): Connecting to remote host via SSH...
# aci_tenant.provisioner_tenant2 (remote-exec):   Host: 10.10.20.14
# aci_tenant.provisioner_tenant2 (remote-exec):   User: admin
# aci_tenant.provisioner_tenant2 (remote-exec):   Password: true
# aci_tenant.provisioner_tenant2 (remote-exec):   Private key: false
# aci_tenant.provisioner_tenant2 (remote-exec):   Certificate: false
# aci_tenant.provisioner_tenant2 (remote-exec):   SSH Agent: true
# aci_tenant.provisioner_tenant2 (remote-exec):   Checking Host Key: false
# aci_tenant.provisioner_tenant2 (remote-exec):   Target Platform: unix
# aci_tenant.provisioner_tenant2 (remote-exec): Connected!
# aci_tenant.provisioner_tenant2 (remote-exec): This command is being deprecated on APIC controller, please use NXOS-style equivalent command
# aci_tenant.provisioner_tenant2 (remote-exec): Heroes infra SnV provisioner_tenant2 provisioner_tenant1 mgmt common
# aci_tenant.provisioner_tenant2: Creation complete after 9s [id=uni/tn-provisioner_tenant2]


# ==========================
# If provisioner doesnt need to be associated with a real resource, we can associate it with 'terraform_data' - this resource does nothing.
# Unfortunately terraform_data is not supported in terraform version used in Lab Exam

# Based on 'Terraform Up and Running, we can also use "null_resource". This requires terraform init, because hashicorp/null provider is needed
# │ failed to instantiate provider "registry.terraform.io/hashicorp/null" to obtain schema: unknown provider "registry.terraform.io/hashicorp/null"

# resource "terraform_data" "tf_data" {
#     provisioner "local-exec" {
#         command = "echo \"Time from terraform_data: ${timestamp()}\""
#     }
# }

# resource "null_resource" "null_provisioner" {
#     provisioner "local-exec" {
#         command = "echo \"Time from null_resource: ${timestamp()}\""
#     }
# }
