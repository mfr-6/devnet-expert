output "configured_vrfs" {
  value       = [for vrf in aci_vrf.mfr_tenant_vrfs : vrf.ip_data_plane_learning]
  description = "List of dataplane learning state of configured VRFs"
}