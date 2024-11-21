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
  password = "!v3G@!4@Y"
  url      = "https://sandboxapicdc.cisco.com/"
  insecure = true
}

locals {
  tenants_aps = flatten([ for tenant in var.data: [ for ap in tenant.aps: { tenant_name = tenant.name, ap_name = ap.name } ] ])
  aps_epgs = flatten([ for tenant in var.data: [ for ap in tenant.aps: [ for epg in ap.epgs: { ap_name = ap.name, epg_name = epg.name } ] ] ])
}


resource "aci_tenant" "aci_tenants" {
  for_each = toset([ for tenant in var.data: tenant.name ])
  name = each.key
}

resource "aci_application_profile" "aci_aps" {
  for_each = { for element in local.tenants_aps: element.ap_name => element }
  name = each.key
  tenant_dn = aci_tenant.aci_tenants[each.value.tenant_name].id
  
}

resource "aci_application_epg" "aci_epgs" {
  for_each = { for element in local.aps_epgs: element.epg_name => element }
  application_profile_dn = aci_application_profile.aci_aps[each.value.ap_name].id
  name = each.key
  
}

#https://stackoverflow.com/questions/58594506/how-to-for-each-through-a-listobjects-in-terraform-0-12
#flatten([ for tenant in local.data : [ for ap in tenant.aps : { tenant = tenant.name, ap = ap.name } ] ])