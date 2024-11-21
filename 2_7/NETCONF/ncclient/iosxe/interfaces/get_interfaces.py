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

# If using filter without subtree tuple - you need to specify xmlns namespace - otherwise it won't work
# interfaces_filter = """
# <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
# </filter>
# """

# with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
#   intf_resp = mgr.get(filter=interfaces_filter)
#   print(intf_resp)
########

# Approach with subtree but without <filter> tag
interfaces_filter = """
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
  intf_resp = mgr.get(filter=("subtree", interfaces_filter))

  data = xmltodict.parse(intf_resp.xml)
  table = PrettyTable()
  table.field_names = ["name", "status", "address", "speed", "in-octets"]
  for intf in data["rpc-reply"]["data"]["interfaces-state"]["interface"]:
    table.add_row([intf["name"], intf["admin-status"], intf["phys-address"], intf["speed"], intf["statistics"]["in-octets"]])
  print(table)
########