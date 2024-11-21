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
  <routing xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
    <routing-instance>
      <name>default</name>
      <routing-protocols>
        <routing-protocol>
          <type>static</type>
          <name>1</name>
          <static-routes>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ipv4-unicast-routing">
              <route>
                <destination-prefix>192.168.4.0/24</destination-prefix>
                <next-hop>
                  <next-hop-address>10.1.1.1</next-hop-address>
                </next-hop>
              </route>
              <route>
                <destination-prefix>192.168.5.0/24</destination-prefix>
                <next-hop>
                  <next-hop-address>10.1.1.1</next-hop-address>
                </next-hop>
              </route>
              <route>
                <destination-prefix>192.168.6.0/24</destination-prefix>
                <next-hop>
                  <next-hop-address>10.1.1.1</next-hop-address>
                </next-hop>
              </route>
            </ipv4>
          </static-routes>
        </routing-protocol>
      </routing-protocols>
    </routing-instance>
  </routing>
</config>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
    response = mgr.edit_config(cfg, target="running")

print(response)
