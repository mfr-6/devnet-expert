locals {
  vrf_names = ["mfr_vrf1", "mfr_vrf2", "mfr_vrf3", "mfr_vrf4", "mfr_vrf5"]
}

# variable "vrf_names_list" {
#   description = "List of VRF names to be configured"
#   type = list(string)
#   default = [ "mfr_vrf1", "mfr_vrf2", "mfr_vrf3", "mfr_vrf4", "mfr_vrf5" ]
# }