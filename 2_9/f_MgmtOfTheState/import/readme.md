Important note: Configure infra based on config placed in parent dir, then play around with TF Import. You can instead create resource in APIC GUI and then import it.

Importing resources into Terraform from ACI

1. Get resource DN from existing resource
```
$ terraform show -json | jq '.values.root_module.resources[0].values.id'
"uni/tn-mfr_tenant1"
```
2. Create resource declaration
```
resource "aci_tenant" "imported_mfr_tenant1" {
    name = "mfr_tenant1"
}
```
3. Import resource with following command:
```
terraform import aci_tenant.imported_mfr_tenant1 uni/tn-mfr_tenant1
aci_tenant.imported_mfr_tenant1: Importing from ID "uni/tn-mfr_tenant1"...
aci_tenant.imported_mfr_tenant1: Import prepared!
  Prepared aci_tenant for import
aci_tenant.imported_mfr_tenant1: Refreshing state... [id=uni/tn-mfr_tenant1]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```
4. Verify if resource is present in statefile.
```
terraform show -json | jq '.values.root_module.resources'
[
  {
    "address": "aci_tenant.imported_mfr_tenant1",
    "mode": "managed",
    "type": "aci_tenant",
    "name": "imported_mfr_tenant1",
    "provider_name": "registry.terraform.io/ciscodevnet/aci",
    "schema_version": 1,
    "values": {
      "annotation": "orchestrator:terraform",
      "description": "",
      "id": "uni/tn-mfr_tenant1",
      "name": "mfr_tenant1",
      "name_alias": "",
      "relation_fv_rs_tenant_mon_pol": null,
      "relation_fv_rs_tn_deny_rule": []
    },
    "sensitive_values": {
      "relation_fv_rs_tn_deny_rule": []
    }
  }
]
```