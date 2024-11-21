variable "infra" {
  description = "List of tenant and child vrfs"
  type        = map(any)
}

locals {
  tenants_vrfs = flatten(
    [
      for tenant, values in var.infra : [
        for vrf in values.vrfs : {
          tenant : tenant,
          vrf : vrf
        }
      ]
    ]
  )
}