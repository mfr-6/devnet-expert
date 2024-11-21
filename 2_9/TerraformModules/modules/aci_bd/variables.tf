variable "tenant_dn" {
  description = "Tenant DN where BD should be created in"
  type        = string
}

variable "vrf_dn" {
  description = "Tenant DN BD will be attached to"
  type        = string
}

variable "bridge_domains" {
  description = "List of BridgeDomain objects"
  type = list(object({
    name               = string
    description        = string
    l2_unknown_unicast = string
  }))
}
