import ncs

with ncs.maapi.single_write_trans("admin", "python", groups=["ncsadmin"]) as t:
  # get top level root object
  root = ncs.maagic.get_root(t)
  # get specific device
  device_cfg = root.devices.device["dist-rtr01"].config
  #delete interface
  del device_cfg.ios__interface.Loopback["1337"]
  t.apply()
  

## RESULT 
# admin@ncs#     
# System message at 2024-02-15 05:36:11...
# Commit performed by admin via tcp using python.
# admin@ncs# show running-config devices device dist-rtr01 config interface Loopback 1337
# --------------------------------------------------------------------------^
# syntax error: unknown argument
# admin@ncs# show running-config devices device dist-rtr01 config interface Loopback     
# devices device dist-rtr01
#  config
#   interface Loopback0
#    description to
#    no ip address
#    shutdown
#   exit
#   interface Loopback100
#    ip address 192.168.1.1 255.255.255.0
#    no shutdown
#   exit
#  !
# !

# changes are applied immediately to device
# dist-rtr01#sh ip int brief
# Interface              IP-Address      OK? Method Status                Protocol
# GigabitEthernet1       10.10.20.175    YES NVRAM  up                    up      
# GigabitEthernet2       172.16.252.21   YES NVRAM  up                    up      
# GigabitEthernet3       172.16.252.25   YES NVRAM  up                    up      
# GigabitEthernet4       172.16.252.2    YES NVRAM  up                    up      
# GigabitEthernet5       172.16.252.10   YES NVRAM  up                    up      
# GigabitEthernet6       172.16.252.17   YES NVRAM  up                    up      
# Loopback0              unassigned      YES unset  administratively down down    
# Loopback100            192.168.1.1     YES manual up                    up      
# dist-rtr01#