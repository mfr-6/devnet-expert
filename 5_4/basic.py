import hvac

vault_address = "192.168.8.101"

client = hvac.Client(
    url=f'http://{vault_address}:8200',
    token='dev-only-token',
)

print(client.is_authenticated())

