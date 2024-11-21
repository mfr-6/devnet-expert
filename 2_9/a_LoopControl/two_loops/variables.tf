locals {
  tenants = ["mfr_tenant1", "mfr_tenant2"]
  vrfs = [
    {
      "vrf_name" : "mfr_tenant1_vrf1"
      "tenant_name" : "mfr_tenant1"
    },
    {
      "vrf_name" : "mfr_tenant2_vrf1"
      "tenant_name" : "mfr_tenant2"
    },
    {
      "vrf_name" : "mfr_tenant1_vrf2"
      "tenant_name" : "mfr_tenant1"
    }
  ]
}