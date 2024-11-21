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

resource "aci_bridge_domain" "mfr_bd1" {
  name      = "mfr_bd1"
  tenant_dn = aci_tenant.mfr_tenant.id
}

resource "aci_application_profile" "mfr_app1" {
  name      = "mfr_app1"
  tenant_dn = aci_tenant.mfr_tenant.id
}

resource "aci_application_epg" "mfr_epg1" {
  application_profile_dn = aci_application_profile.mfr_app1.id
  name                   = "mfr_epg1"
  relation_fv_rs_bd      = aci_bridge_domain.mfr_bd1.id
}

resource "aci_subnet" "mfr_epg1_subnet1" {
  ip        = "10.0.0.1/32"
  ctrl      = ["no-default-gateway"]
  parent_dn = aci_application_epg.mfr_epg1.id
}

resource "aci_rest" "mfr_epg1_subnet1_dp_learning" {
  path       = "/api/node/mo/${aci_subnet.mfr_epg1_subnet1.id}.json"
  class_name = "fvSubnet"
  content = {
    "ipDPLearning" = "disabled" #enabled
  }

  depends_on = [aci_subnet.mfr_epg1_subnet1]
}

resource "aci_tenant" "new-tenant" {
  name = "new-tenant"
}
