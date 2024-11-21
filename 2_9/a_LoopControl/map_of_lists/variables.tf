locals {
  tenants_and_vrfs = {
    "mfr_tenant1" : ["mfr_tenant1_vrf1", "mfr_tenant1_vrf2", "mfr_tenant1_vrf3"]
    "mfr_tenant2" : ["mfr_tenant2_vrf1", "mfr_tenant2_vrf2"]
  }

  vrfs = flatten(
    [
      for tenant, vrfs in local.tenants_and_vrfs : [
        for vrf in vrfs : {
          tenant = tenant
          name   = vrf
        }
      ]
    ]
  )
}