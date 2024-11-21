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

cfg = """
<config>
  <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
    <bd-items>
      <bd-items>
        <BD-list>
          <fabEncap>vlan-999</fabEncap>
          <name>SUPER_PROD_999</name>
        </BD-list>
      </bd-items>
    </bd-items>
  </System>
</config>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
    cfg_resp = mgr.edit_config(cfg, target="running")

    data = xmltodict.parse(cfg_resp.xml)
    print(json.dumps(data, indent=4))