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

resource "aci_tenant" "aci_tenants" {
  for_each = toset(keys(var.infra))
  name     = each.key
}

resource "aci_vrf" "aci_vrfs" {
  for_each  = { for element in local.tenants_vrfs : element.vrf => element }
  name      = each.key
  tenant_dn = aci_tenant.aci_tenants[each.value.tenant].id

}