import hvac
# https://hvac.readthedocs.io/en/v0.11.2/usage/secrets_engines/kv_v2.html#create-update-secret

vault_address = "192.168.8.101"

client = hvac.Client(
    url=f'http://{vault_address}:8200',
    token='dev-only-token',
)

print(f"Auth status: {client.is_authenticated()}")
print("Creating credentials for ACI Sandbox...")
response = client.secrets.kv.v2.create_or_update_secret(
    path="sandbox_aci_credentials",
    secret=dict(username="admin", password="!v3G@!4@Y")
)

print(f"Done. Status: {response}")
print('Secrets created successfully')
