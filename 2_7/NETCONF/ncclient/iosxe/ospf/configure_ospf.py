from ncclient import manager
import xmltodict


device = {
    "host": "10.10.20.48",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345",
    "type": "iosxe"
}

cfg = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <router>
      <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
        <ospf>
          <process-id xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="create">
            <id>100</id>
            <network>
              <ip>10.1.1.1</ip>
              <wildcard>0.0.0.0</wildcard>
              <area>0</area>
            </network>
          </process-id>
        </ospf>
      </router-ospf>
    </router>
  </native>
</config>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
    cfg_resp = mgr.edit_config(cfg, target="running")

print(cfg_resp)

