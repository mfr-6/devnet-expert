import ncs

with ncs.maapi.single_write_trans("admin", "python", groups=["ncsadmin"]) as t:
  # get top level root object
  root = ncs.maagic.get_root(t)
  # get specific device
  device_cfg = root.devices.device["dist-rtr01"].config
  #print(dir(device.config.ios__interface))
  #create interface
  device_cfg.ios__interface["Loopback"].create("1337")
  device_cfg.ios__interface.Loopback["1337"].description = "test"
  device_cfg.ios__interface.Loopback["1337"].ip.address.primary.address = "192.168.10.1"
  device_cfg.ios__interface.Loopback["1337"].ip.address.primary.mask = "255.255.255.0"
  t.apply()
  

## RESULT 
# admin@ncs# show running-config devices device dist-rtr01 config interface Loopback 1337         
# devices device dist-rtr01
#  config
#   interface Loopback1337
#    description test
#    ip address 192.168.10.1 255.255.255.0
#    no shutdown
#   exit
#  !
# !