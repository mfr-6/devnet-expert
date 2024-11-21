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

# Approach with subtree but without <filter> tag
bgp_filter = """
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <router>
      <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
        <id>65000</id>
      </bgp>
    </router>
  </native>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
  intf_resp = mgr.get(filter=("subtree", bgp_filter))

  data = xmltodict.parse(intf_resp.xml)
  print(json.dumps(data, indent=4))