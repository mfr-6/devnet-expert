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

resource "aci_tenant" "mfr_tenant" {
  name = "mfr_tenant"
}

resource "aci_vrf" "mfr_tenant_vrfs" {
  for_each  = { for i, vrf in local.vrfs : i => vrf }
  name      = each.value.name
  tenant_dn = aci_tenant.mfr_tenant.id
}

