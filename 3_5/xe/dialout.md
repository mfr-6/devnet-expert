```
telemetry ietf subscription 20
 encoding encode-kvgpb
 filter xpath "/process-memory-ios-xe-oper:memory-usage-processes/memory-usage-process[pid='197'][name='IP ARP Retry Ager']"
 stream yang-push
 update-policy periodic 100
 receiver ip address 10.10.20.50 57500 protocol grpc-tcp
 ```