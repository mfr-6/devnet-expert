output "configured_vrfs" {
  value       = [for vrf in aci_vrf.mfr_tenant_vrfs : vrf.id]
  description = "List of DN of configured VRFs"
  sensitive   = false # even though we set this to true, values are in plaintext in tfstate
}