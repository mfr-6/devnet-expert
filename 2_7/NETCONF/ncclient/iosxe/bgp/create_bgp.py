import xmltodict
import json
from ncclient import manager


device = {
    "host": "10.10.20.48",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345",
    "type": "iosxe"
}

bgp_filter = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <router>
      <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
        <id>65000</id>
        <neighbor>
          <id>10.10.10.1</id>
          <remote-as>65001</remote-as>
        </neighbor>
        <neighbor>
          <id>10.10.10.2</id>
          <remote-as>65002</remote-as>
        </neighbor>
      </bgp>
    </router>
  </native>
</config>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
  intf_resp = mgr.edit_config(bgp_filter, target="running")

  data = xmltodict.parse(intf_resp.xml)
  print(json.dumps(data, indent=4))