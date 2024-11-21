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
  #password = "!v3G@!4@Y"
  #url      = "https://sandboxapicdc.cisco.com/"
  password = "C1sco12345"
  url      = "https://10.10.20.14"
  insecure = true
}

resource "aci_tenant" "mfr_tenant1" {
  name = "mfr_tenant1"
}

resource "aci_vrf" "mfr_tenant1_vrf1" {
  name      = "mfr_tenant1_vrf1"
  tenant_dn = aci_tenant.mfr_tenant1.id
}

module "aci_bd" {
  source         = "./modules/aci_bd"
  tenant_dn      = aci_tenant.mfr_tenant1.id
  vrf_dn         = aci_vrf.mfr_tenant1_vrf1.id
  bridge_domains = var.bridge_domains
}

