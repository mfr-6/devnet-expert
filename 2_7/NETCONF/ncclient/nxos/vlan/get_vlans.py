import json
import xmltodict
from ncclient import manager
from prettytable import PrettyTable


device = {
    "host": "10.10.20.40",
    "port": "830",
    "username": "admin",
    "password": "RG!_Yw200",
    "type": "nexus"
}

filter = """
  <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
    <bd-items>
      <bd-items>
        <BD-list/>
      </bd-items>
    </bd-items>
  </System>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
    cfg_resp = mgr.get(filter=("subtree", filter))

    data = xmltodict.parse(cfg_resp.xml)
    table = PrettyTable()
    table.field_names = ["VLAN_ID", "FAB_ENCAP", "NAME", "adminSt"]
    for vlan in data["rpc-reply"]["data"]["System"]["bd-items"]["bd-items"]["BD-list"]:
       table.add_row([vlan.get("id"), vlan.get("fabEncap"), vlan.get("BdOperName"), vlan.get("adminSt")])

    print(table.get_string(sortby="VLAN_ID"))

