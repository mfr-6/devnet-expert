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
  <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
    <intf-items>
      <phys-items>
        <PhysIf-list>
          <id>eth1/14</id>
          <descr>conf by NETCONF in py script</descr>
        </PhysIf-list>
        <PhysIf-list>
          <id>eth1/15</id>
          <descr>conf by NETCONF in py script</descr>
        </PhysIf-list>
          <PhysIf-list>
          <id>eth1/16</id>
          <descr>conf by NETCONF in py script</descr>
        </PhysIf-list>
          <PhysIf-list>
          <id>eth1/17</id>
          <descr>conf by NETCONF in py script</descr>
        </PhysIf-list>
      </phys-items>
    </intf-items>
  </System>
</config>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
    cfg_resp = mgr.edit_config(cfg, target="running")

    data = xmltodict.parse(cfg_resp.xml)
    print(json.dumps(data))

