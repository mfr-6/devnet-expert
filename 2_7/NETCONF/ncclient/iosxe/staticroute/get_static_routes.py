import xmltodict
import json
from ncclient import manager
from prettytable import PrettyTable


device = {
    "host": "10.10.20.48",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345",
    "type": "iosxe"
}

interfaces_filter = """
<routing xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
  <routing-instance>
    <routing-protocols>
      <routing-protocol>
        <static-routes/>
      </routing-protocol>
    </routing-protocols>
  </routing-instance>
</routing>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
  intf_resp = mgr.get(filter=("subtree", interfaces_filter))

  data = xmltodict.parse(intf_resp.xml)
  table = PrettyTable()
  table.field_names = ["destination"]
  for route in data["rpc-reply"]["data"]["routing"]["routing-instance"]["routing-protocols"]["routing-protocol"]["static-routes"]["ipv4"]["route"]:
      table.add_row([route["destination-prefix"]])



print(table)
