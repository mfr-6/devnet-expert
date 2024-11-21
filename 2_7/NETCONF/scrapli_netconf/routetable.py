import hvac
import xmltodict
import json
from scrapli_netconf.driver import NetconfDriver

client = hvac.Client(
    url='http://localhost:8200',
    token="test-token"
)

#print(client.is_authenticated())

secrets = client.secrets.kv.v2.read_secret_version(mount_point="sbx", path="iosxe")["data"]["data"]
#r = client.secrets.kv.v2.create_or_update_secret(mount_point="sbx", path="test123",secret=dict(passwd="1234"))
#print(r)


my_device = {
    "host": "10.10.20.48",
    "auth_username": secrets.get("username"),
    "auth_password": secrets.get("password"),
    "auth_strict_key": False,
    "port": 830
}

rt_filter = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <ip>
      <route>
        <ip-route-interface-forwarding-list/>
      </route>
    </ip>
  </native>
</filter>
"""

with NetconfDriver(**my_device) as conn:
  response = conn.get_config(source="running", filter_type="subtree", filter_=rt_filter)
#

data = xmltodict.parse(response.result)

print(json.dumps(data, indent=4))

#print(response.result)