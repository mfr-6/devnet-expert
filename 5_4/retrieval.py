import hvac
# Used version is

vault_address = "192.168.8.101"

client = hvac.Client(
    url=f'http://{vault_address}:8200',
    token='dev-only-token',
)

print(f"Auth status: {client.is_authenticated()}")
print("Credentials retrieval...")

read_response = client.secrets.kv.read_secret_version(path='sandbox_aci_credentials')
print(f"Username: {read_response['data']['data']['username']}")
print(f"Password: {read_response['data']['data']['password']}")
#print(read_response)

