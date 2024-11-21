
### Log in to Influx DB

```
root@a9b27ca62069:/# influx
Connected to http://localhost:8086 version 1.8.10
InfluxDB shell version: 1.8.10
> 
```

### Display databases
```
> show databases
name: databases
name
----
_internal
mdt_grpc
mdt_grpc_tls
mdt_netconf
mdt_restconf
mdt_snmp
mdt_gnmi
> 
```

### ???

```
> use mdt_grpc
Using database mdt_grpc
> show measurements
name: measurements
name
----
Cisco-IOS-XE-process-cpu-oper:cpu-usage/cpu-utilization
> 
```

