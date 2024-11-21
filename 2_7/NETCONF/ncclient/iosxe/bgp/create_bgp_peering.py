import xmltodict
import json
from ncclient import manager


device_xe = {
    "host": "10.10.20.48",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345",
    "type": "iosxe"
}

device_nx = {
    "host": "10.10.20.40",
    "port": "830",
    "username": "admin",
    "password": "RG!_Yw200",
    "type": "nexus"
}

bgp_cfg_xe = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <router>
      <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
        <id>65001</id>
        <neighbor>
          <id>10.10.20.40</id>
          <remote-as>65002</remote-as>
        </neighbor>
      </bgp>
    </router>
  </native>
</config>
"""

bgp_cfg_nx = """
<config>
  <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
    <fm-items>
      <bgp-items>
        <adminSt>enabled</adminSt>
      </bgp-items>
    </fm-items>
    <bgp-items>
      <inst-items>
        <asn>65002</asn>
        <dom-items>
          <Dom-list>
            <name>default</name>
            <peer-items>
              <Peer-list>
                <addr>10.10.20.40</addr>
                <asn>65001</asn>
              </Peer-list>
            </peer-items>
          </Dom-list>
        </dom-items>
      </inst-items>
    </bgp-items>
  </System>
</config>
"""

with manager.connect(host=device_xe["host"], port=device_xe["port"], username=device_xe["username"], password=device_xe["password"]) as mgr:
  intf_resp = mgr.edit_config(bgp_cfg_xe, target="running")

  data = xmltodict.parse(intf_resp.xml)
  print(f"!!!!!!!!! XE RESULT: {json.dumps(data, indent=4)}")

with manager.connect(host=device_nx["host"], port=device_nx["port"], username=device_nx["username"], password=device_nx["password"]) as mgr:
  intf_resp = mgr.edit_config(bgp_cfg_nx, target="running")

  data = xmltodict.parse(intf_resp.xml)
  print(f"!!!!!!!!! NX RESULT: {json.dumps(data, indent=4)}")