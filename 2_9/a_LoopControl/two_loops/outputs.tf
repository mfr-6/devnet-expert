output "configured_tenants" {
  value       = { for index, tenant in aci_tenant.mfr_tenants : tenant.id => { for index, vrf in aci_vrf.mfr_tenant_vrfs : "vrfs" => vrf.name... if vrf.tenant_dn == tenant.id } }
  description = "List of configured with all child VRFs"
}

# Outputs:

# configured_tenants = {
#   "uni/tn-mfr_tenant1" = {
#     "vrfs" = [
#       "mfr_tenant1_vrf1",
#       "mfr_tenant1_vrf2",
#     ]
#   }
#   "uni/tn-mfr_tenant2" = {
#     "vrfs" = [
#       "mfr_tenant2_vrf1",
#     ]
#   }
# }

# Ellipsis allows us to enable grouping mode allowing duplicates
# https://developer.hashicorp.com/terraform/language/expressions/for#for-expressions