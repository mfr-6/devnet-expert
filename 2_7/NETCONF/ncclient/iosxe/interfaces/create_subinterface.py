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
    <interface>
      <GigabitEthernet>
        <name>3</name>
        <shutdown xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="delete"/>
      </GigabitEthernet>
      <GigabitEthernet xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="create">
        <name>3.110</name>
        <description>Created via ncclient</description>
        <encapsulation>
          <dot1Q>
            <vlan-id>110</vlan-id>
          </dot1Q>
        </encapsulation>
        <ip>
          <address>
            <primary>
              <address>10.110.1.1</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
      </GigabitEthernet>
    </interface>
  </native>
</config>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
    response = mgr.edit_config(cfg, target="running")

print(response)
