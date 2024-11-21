## Required providers

https://developer.hashicorp.com/terraform/language/providers/requirements#version-constraints

Useful commands:

1. Terraform fmt -recursive (recursively perform formatting)
2. Terraform validate -> validate configuration
3. terraform apply -auto-approve -> run apply without confirmation
4. terraform output -> print outputs previously saved to statefile (add -json flag for json output)
5. terraform console -> interactive console (works only if tf is initialized) to test expressions (tf console LOCKS STATEFILE!!!)
```
(main) expert@expert-cws:~/src/tasks/devnet-expert/2_9/a_LoopControl/foreach$ terraform console
> aci_vrf.mfr_tenant_vrfs["mfr_vrf1"].id
"uni/tn-mfr_tenant/ctx-mfr_vrf1"
```
6. Get list of unique resources created
```
(main) expert@expert-cws:~/src/tasks/devnet-expert/2_9/f_MgmtOfTheState$ terraform show -json | jq '.values.root_module.resources | map(.type) | unique'
[
  "aci_tenant",
  "aci_vrf"
]
```

Useful features:

Terraform VS Code extension - autocompletion required resource arguments:

1. Go to HashiCorp Terraform settings
2. Terraform-ls: Experimental Features
3. Go to "Edit in settings.json"
4. Add "prefillRequiredFields" settings under "terraform-ls.experimentalFeatures".
    "terraform-ls.experimentalFeatures": {
        "prefillRequiredFields": true
    }
5. Save and restart VS Code




!!! Outputs are saved to statefile. In order to print them, use: terraform output

  "terraform_version": "1.0.11",
  "serial": 9,
  "lineage": "e9b681b1-0594-1018-52e2-cfe6bcb738e0",
  "outputs": {
    "configured_vrfs": {
      "value": [
        "uni/tn-mfr_tenant/ctx-mfr_vrf1",
        "uni/tn-mfr_tenant/ctx-mfr_vrf2",
        "uni/tn-mfr_tenant/ctx-mfr_vrf3",
        "uni/tn-mfr_tenant/ctx-mfr_vrf4",
        "uni/tn-mfr_tenant/ctx-mfr_vrf5"
      ],
      "type": [
        "tuple",
        [
          "string",
          "string",
          "string",
          "string",
          "string"
        ]
      ]
    }
  },






