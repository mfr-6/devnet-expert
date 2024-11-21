import click
import requests
import json
import re

requests.packages.urllib3.disable_warnings()

from jinja2 import Template
from ncclient import manager

class OspfRouter():
  intf_type = None
  intf_ip_addr = None
  physical_intf_number = None
  subintf_vlan = None

  def render_netconf(self):
    with open("templates/ospf-6241.j2", "r") as templ:
      ospf_netconf_template = Template(templ.read())
    netconf_data = ospf_netconf_template.render({
    "intf_type": self.intf_type,
    "physical_intf_number": self.physical_intf_number,
    "subintf_vlan": self.subintf_vlan,
    "intf_ip_addr": self.intf_ip_addr
    })
    
    return netconf_data

  def render_restconf(self):
    with open("templates/ospf-8040.j2", "r") as templ:
      ospf_restconf_template = Template(templ.read())
    restconf_data = ospf_restconf_template.render({"ospf": {
    "intf_type": self.intf_type,
    "physical_intf_number": self.physical_intf_number,
    "subintf_vlan": self.subintf_vlan,
    "intf_ip_addr": self.intf_ip_addr
    }})
    return restconf_data


@click.group()
def expertconf():
  pass

@expertconf.group()
def add():
  pass

@add.command()
@click.argument("router_address")
@click.argument("username")
@click.option("--ethsubintf", required=True, help="Full name of Ethernet subinterface. Example: GigabitEthernet2.991")
@click.option("--intfaddr", "--ip", required=True, help="IP address of new subinterface. Example: 10.38.99.1")
@click.option("--rfc", type=click.Choice(["8040", "6241"]), required=True)
@click.option('--password', prompt=True, hide_input=True)
def ospf(router_address, username, ethsubintf, intfaddr, rfc, password):
  router = OspfRouter()
  parsed_intf = re.match(r"(\D+)(\d).(\d+)", ethsubintf)

  router.intf_type = parsed_intf[1]
  router.intf_ip_addr = intfaddr
  router.physical_intf_number = parsed_intf[2]
  router.subintf_vlan = parsed_intf[3]
  if rfc == "6241":
    config = router.render_netconf()
    print(config)
    print(type(config))
    with manager.connect(host=router_address, port="830", username=username, password=password, hostkey_verify=False, device_params={"name": "iosxe"}) as mgr:
      reply = mgr.edit_config(config, target="running")
    print(reply)
  elif rfc == "8040":
    config = router.render_restconf()
    url = f"https://{router_address}/restconf/data/Cisco-IOS-XE-native:native"
    headers = {
      "Content-Type": "application/yang-data+json",
      "Accept": "application/yang-data+json"
    }
    rsp = requests.patch(url=url, headers=headers, json=json.loads(config), auth=(username, password), verify=False)
    rsp.raise_for_status()

if __name__ == "__main__":
  expertconf()



