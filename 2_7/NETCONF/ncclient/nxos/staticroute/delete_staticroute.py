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
  <network-instances xmlns="http://openconfig.net/yang/network-instance">
    <network-instance>
      <name>default</name>
      <protocols>
        <protocol>
          <identifier>STATIC</identifier>
          <name>DEFAULT</name>
          <static-routes>
            <static xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="delete">
              <prefix>10.20.30.40</prefix>
              <config>
                <prefix>10.20.30.40</prefix>
              </config>
              <next-hops>
                <next-hop>
                  <index>+2.2.2.2+default</index>
                  <config>
                    <next-hop>2.2.2.2</next-hop>
                  </config>
                </next-hop>
              </next-hops>
            </static>
          </static-routes>
        </protocol>
      </protocols>
    </network-instance>
  </network-instances>
</config>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
    cfg_resp = mgr.edit_config(cfg, target="running")

    data = xmltodict.parse(cfg_resp.xml)
    print(json.dumps(data, indent=4))

