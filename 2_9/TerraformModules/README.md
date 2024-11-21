### Issues

Sometimes Terraform pukes Errors:

Plan: 3 to add, 0 to change, 0 to destroy.
aci_tenant.mfr_tenant1: Creating...
╷
│ Error: invalid character '<' looking for beginning of value
│ 
│   with aci_tenant.mfr_tenant1,
│   on main.tf line 17, in resource "aci_tenant" "mfr_tenant1":
│   17: resource "aci_tenant" "mfr_tenant1" {
│ 

or 

aci_tenant.mfr_tenant1: Creating...
aci_tenant.mfr_tenant1: Creation complete after 6s [id=uni/tn-mfr_tenant1]
module.aci_bd.aci_bridge_domain.aci_bd["0"]: Creating...
module.aci_bd.aci_bridge_domain.aci_bd["1"]: Creating...
╷
│ Error: invalid character '<' looking for beginning of value
│ 
│   with module.aci_bd.aci_bridge_domain.aci_bd["0"],
│   on modules/aci_bd/main.tf line 1, in resource "aci_bridge_domain" "aci_bd":
│    1: resource "aci_bridge_domain" "aci_bd" {
│ 
╵
╷
│ Error: invalid character '<' looking for beginning of value
│ 
│   with module.aci_bd.aci_bridge_domain.aci_bd["1"],
│   on modules/aci_bd/main.tf line 1, in resource "aci_bridge_domain" "aci_bd":
│    1: resource "aci_bridge_domain" "aci_bd" {
│ 
╵

I assume this is ACI Provider issue (0.7 - it's so old). After multiple times - resources are eventualy created (without changing existing TF configuration).

Problems mentioned above are present on AlwaysOn APIC only. All good when configuring APIC from Sandbox reserved lab.