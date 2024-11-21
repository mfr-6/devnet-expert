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

## THIS IS NOT WORKING - to be verified # TODO:
interfaces_filter = """
  <filter type="cli" >
    <config-format-xml options="all"></config-format-xml>
  </filter>
"""

with manager.connect(host=device["host"], port=device["port"], username=device["username"], password=device["password"]) as mgr:
  cfg_resp = mgr.get(filter=interfaces_filter)

  data = xmltodict.parse(cfg_resp.xml)
  print(json.dumps(data, indent=4))
########