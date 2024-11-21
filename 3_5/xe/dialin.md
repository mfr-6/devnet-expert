# NETCONF

/etc/telegraf/telegraf.conf
```
[[inputs.cisco_telemetry_mdt_netconf_dialin]]
  server_address = "10.10.20.48:830"
  username = "developer"
  password = "C1sco12345"
  ignore_server_authenticity = true
  redial = "60s"

[[inputs.cisco_telemetry_mdt_netconf_dialin.subscription]]
  xpath_filter = "/interfaces-ios-xe-oper:interfaces/interface[name='GigabitEthernet1']/statistics/in-octets"
  update_trigger = "periodic"
  period = "1s"
```



[[inputs.gnmi]]
  addresses = ["10.10.20.35:57100"]
  username = "admin"
  password = "C1sco12345"

[[inputs.gnmi.subscription]]
  name = "cpu-one-min"
  origin = "Cisco-IOS-XR-wdsysmon-fd-oper"
  path = "/system-monitoring/cpu-utilization/total-cpu-one"
  subscription_mode = "sample"
  sample_interval = "1s"


[[outputs.influxdb]]
  database = "mdt_gnmi"
  urls = [ "http://127.0.0.1:8086" ]
