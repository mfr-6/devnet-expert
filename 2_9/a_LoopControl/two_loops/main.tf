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

resource "aci_tenant" "mfr_tenants" {
  for_each = toset(local.tenants)
  name     = each.value
}

resource "aci_vrf" "mfr_tenant_vrfs" {
  for_each  = { for vrf in local.vrfs : vrf.vrf_name => vrf.tenant_name }
  name      = each.key
  tenant_dn = aci_tenant.mfr_tenants[each.value].id
}

