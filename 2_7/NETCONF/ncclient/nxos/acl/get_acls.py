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

acl_filter = """
  <acl xmlns="http://openconfig.net/yang/acl">
    <acl-sets>
      <acl-set>
        <name>x</name>
        <type>x</type>
      </acl-set>
    </acl-sets>
  </acl>

  <network-instances xmlns="http://openconfig.net/yang/network-instance">
    <network-instance>
      <name>default</name>
      <protocols>
        <protocol>
          <identifier>STATIC</identifier>
          <name>DEFAULT</name>
          <static-routes>
          </static-routes>
        </protocol>
      </protocols>
    </network-instance>
  </network-instances>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
    cfg_resp = mgr.get(filter=("subtree", acl_filter))

    data = xmltodict.parse(cfg_resp.xml)
    print(json.dumps(data, indent=4))


