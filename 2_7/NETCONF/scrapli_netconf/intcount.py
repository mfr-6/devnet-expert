import xmltodict
import json
from scrapli_netconf.driver import NetconfDriver

sbx_inventory = {
  "ip": "10.10.20.48",
  "username": "developer",
  "password": "C1sco12345"
}

sbx = {
    "host": sbx_inventory.get("ip"),
    "auth_username": sbx_inventory.get("username"),
    "auth_password": sbx_inventory.get("password"),
    "auth_strict_key": False,
    "port": 830
}

int_filter = """
<filter>
  <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
    <interface>
      <name>GigabitEthernet1</name>
      <statistics/>
    </interface>
  </interfaces>
</filter>
"""

with NetconfDriver(**sbx) as connection:
  resp = connection.get(filter_=int_filter)

data = xmltodict.parse(resp.result)
interfaces_data = data.get("rpc-reply").get("data").get("interfaces")
#print(json.dumps(data, indent=4))
print(f"Interface name: {interfaces_data.get('interface').get('name')}")
print(f"Interface input packets: {interfaces_data.get('interface').get('statistics').get('in-unicast-pkts')}")
#print(resp.result)