Spin up docker container with hashicorp vault

```
docker run -itd --name vault -v vault_file:/vault/file -v vault_logs:/vault/logs -e VAULT_DEV_ROOT_TOKEN_ID="1234QWer!" -p 8200:8200 hashicorp/vault:1.8
```
1.8.0, because 1.8 is mentioned in Exam Software list

Warning: The root token is useful for development, but allows full access to all data and functionality of Vault, so it must be carefully guarded in production. Ideally, even an administrator of Vault would use their own token with limited privileges instead of the root token. 
https://developer.hashicorp.com/vault/docs/get-started/developer-qs#step-1-start-vault

HVAC version: hvac==0.11.2
Docs: https://hvac.readthedocs.io/en/v0.11.2/overview.html


1. When executing "client.secrets.kv.v2.create_or_update_secret()" if something changed has been sent to vault, then vault creates a new Version of a secret.
2. It's not idempotent, meaning that sending same data bumps secret version anyways.

`mount_point` is used to specify non-default KV store. It's available on every kv method.
`r = client.secrets.kv.v2.create_or_update_secret(mount_point="sbx", path="test123",secret=dict(passwd="1234"))`
