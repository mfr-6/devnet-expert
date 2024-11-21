import json
import xmltodict
from ncclient import manager


device = {
    "host": "10.10.20.40",
    "port": "830",
    "username": "admin",
    "password": "RG!_Yw200",
    "type": "nexus"
}

filter = """
<filter>
  <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
    <intf-items>
      <phys-items>
        <PhysIf-list>
          <id/>
          <descr/>
        </PhysIf-list>
      </phys-items>
    </intf-items>
  </System>
</filter>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
    cfg_resp = mgr.get(filter)#, source="running")

    data = xmltodict.parse(cfg_resp.xml)
    print(json.dumps(data, indent=4))
    for intf in data["rpc-reply"]["data"]["System"]["intf-items"]["phys-items"]["PhysIf-list"]:
        print(intf.get("descr"), intf.get("descr"))

