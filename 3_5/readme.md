## TIG Stack

### Spin up TIG Stack
```
docker pull jeremycohoe/tig_mdt
docker run -ti -p 3000:3000 -p 57500:57500 jeremycohoe/tig_mdt
```

## Grafana

### Reset admin password

```
root@a9b27ca62069:~# grafana-cli --homepath "/usr/share/grafana/" admin reset-admin-password admin
INFO [03-01|04:11:06] Starting Grafana                         logger=settings version= commit= branch= compiled=1970-01-01T00:00:00Z
WARN [03-01|04:11:06] "sentry" frontend logging provider is deprecated and will be removed in the next major version. Use "grafana" provider instead. logger=settings
INFO [03-01|04:11:06] Config loaded from                       logger=settings file=/usr/share/grafana/conf/defaults.ini
INFO [03-01|04:11:06] Config loaded from                       logger=settings file=/etc/grafana/grafana.ini
INFO [03-01|04:11:06] Config overridden from command line      logger=settings arg="default.paths.data=/var/lib/grafana"
INFO [03-01|04:11:06] Config overridden from command line      logger=settings arg="default.paths.logs=/var/log/grafana"
INFO [03-01|04:11:06] Config overridden from command line      logger=settings arg="default.paths.plugins=/var/lib/grafana/plugins"
INFO [03-01|04:11:06] Config overridden from command line      logger=settings arg="default.paths.provisioning=/etc/grafana/provisioning"
INFO [03-01|04:11:06] Path Home                                logger=settings path=/usr/share/grafana/
INFO [03-01|04:11:06] Path Data                                logger=settings path=/var/lib/grafana
INFO [03-01|04:11:06] Path Logs                                logger=settings path=/var/log/grafana
INFO [03-01|04:11:06] Path Plugins                             logger=settings path=/var/lib/grafana/plugins
INFO [03-01|04:11:06] Path Provisioning                        logger=settings path=/etc/grafana/provisioning
INFO [03-01|04:11:06] App mode production                      logger=settings
INFO [03-01|04:11:06] Connecting to DB                         logger=sqlstore dbtype=sqlite3
INFO [03-01|04:11:06] Starting DB migrations                   logger=migrator
INFO [03-01|04:11:06] migrations completed                     logger=migrator performed=0 skipped=481 duration=484.218µs
INFO [03-01|04:11:06] Envelope encryption state                logger=secrets enabled=true current provider=secretKey.v1

Admin password changed successfully ✔
```






### Import dashboard
https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/import-dashboards/

## Dial-in

Netconf needs to be enables on a IOS XE device. Once done - Dial-in connectio can be created. NETCONF and gNMI are used for Dial-in method.

### NETCONF

Enable Netconf
```
netconf-yang
```

NETCONF needs to have priv 15
```
configure terminal
aaa new-model
aaa authentication login default local
aaa authorization exec default local 
aaa session-id common

username admin privilege 15 password 0 Cisco123
```

### Dial-out
### Useful links

https://github.com/jeremycohoe/cisco-ios-xe-mdt


```
cat8000v#show telemetry ietf subscription 10 detail 
Telemetry subscription detail:

  Subscription ID: 10
  Type: Configured
  State: Valid
  Stream: yang-push
  Filter:
    Filter type: xpath
    XPath: /memory-ios-xe-oper:memory-statistics/memory-statistic/used-memory
  Update policy:
    Update Trigger: periodic
    Period: 100
  Encoding: encode-kvgpb
  Source VRF: 
  Source Address: 
  Notes: Subscription validated

  Named Receivers:
    Name                                              Last State Change  State                 Explanation                                                   
    -------------------------------------------------------------------------------------------------------------------------------------------------------
    grpc-tcp://192.168.254.11:57500                   03/02/24 11:28:18  Transport requested                                                                 
          

cat8000v#
```


```

cat8000v#show telemetry ietf subscription 10 receiver
Telemetry subscription receivers detail:

  Subscription ID: 10
  Name: grpc-tcp://192.168.254.11:57500
  Connection: 43
  State: Transport requested
  Explanation: 
  Last Error: Transport lost
  Target State: Connected
```



ssh -oHostKeyAlgorithms=+ssh-dss developer@10.10.20.35



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




XR Config Dial-Out
```
telemetry model-driven
 destination-group SBX
  address-family ipv4 10.10.20.50 port 57500
   encoding gpb
   protocol grpc
  !
 !
 sensor-group SG1
  sensor-path Cisco-IOS-XR-wdsysmon-fd-oper:system-monitoring/cpu-utilization/total-cpu-one-minute
 !
 subscription Subscription1
  sensor-group-id SG1 sample-interval 1000
  destination-id SBX
 !
!
```
```
RP/0/RP0/CPU0:xrv9k#show telemetry model-driven subscription 
Sat Mar  2 14:47:13.231 UTC
Subscription:  Subscription1            State: NA
-------------
  Sensor groups:
  Id                               Interval(ms)        State     
  SG1                              1000                Not Resolved

  Destination Groups:
  Id                 Encoding            Transport   State   Port    Vrf     IP            
  SBX                gpb                 grpc        NA      57500           10.10.20.50   
```