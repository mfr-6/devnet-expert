# Creating compliance reports

Use cases:
1. Build device template that contains desired config to test
2. Build a compliance report to check the configuration of a group of devices against a template

Building device template
1. Create device template
```
devices template COMPLIANCE-CHECK
 ned-id cisco-ios-cli-6.91
 config
 ip name-server name-server-list 208.67.222.222
 ip name-server name-server-list 208.67.220.220
 exit
 service timestamps log datetime localtime show-timezone year
 logging host ipv4 10.225.1.11
 exit
 ntp server peer-list 10.225.1.11
 exit
 exit
 exit
 !
 ned-id cisco-nx-cli-5.23
 config
 ip name-server servers 208.67.222.222
 ip name-server servers 208.67.220.220
 logging timestamp milliseconds
 logging server 10.225.1.11 level 5
 exit
 ntp server 10.225.1.11
 exit
 exit
 exit
 !
 ned-id cisco-asa-cli-6.6
 config
 dns domain-lookup mgmt
 dns server-group DefaultDNS
 name-server 208.67.222.222
 name-server 208.67.220.220
 exit
 logging timestamp
 logging host mgmt 10.225.1.11
 exit
 ntp server 10.225.1.11
 exit
 exit
 exit
```

2. Build compliance report 
```
compliance reports report <report-name>
compare-template <template-name> <device-group>
commit
```

3. Execute compliance report
Report can be executed via CLI or NSO GUI.

```
admin@ncs# compliance reports report COMPLIANCE-CHECK run
time 2024-02-02T05:59:14.076108+00:00
compliance-status violations
info Checking no devices and no services
location http://localhost:8080/compliance-reports/report_2024-02-02T05:59:14.076108+00:00.xml
```

We can generate report in different formats
```
compliance reports report COMPLIANCE-CHECK run outformat text
compliance reports report COMPLIANCE-CHECK run outformat html
```