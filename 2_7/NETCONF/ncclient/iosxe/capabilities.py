from ncclient import manager

device = {
    "host": "10.10.20.48",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345",
    "type": "iosxe"
}

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
    for capability in mgr.server_capabilities:
        print(capability)

