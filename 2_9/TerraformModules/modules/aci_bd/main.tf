resource "aci_bridge_domain" "aci_bd" {
  for_each           = { for k, v in var.bridge_domains : k => v }
  tenant_dn          = var.tenant_dn
  relation_fv_rs_ctx = var.vrf_dn
  name               = each.value.name
  description        = "${each.value.description} ${timestamp()}"
  unk_mac_ucast_act  = each.value.l2_unknown_unicast == "" ? "proxy" : each.value.l2_unknown_unicast # When value is not provided - set default (proxy)
}
