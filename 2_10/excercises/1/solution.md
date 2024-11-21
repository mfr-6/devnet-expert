1. `source ~/local-nso/ncsrc`
2. Create local NSO instance `ncs-setup --package ~/local-nso/packages/neds/cisco-ios-cli-6.103 --dest ~/nso-instance-1`
3. Create netsim
ncs-netsim add-to-network ~/local-nso/packages/neds/cisco-nx-cli-5.25 1 nxos --dir ./netsim
a) Create network with 1 device where name starts with "xe" and save it to ./netsim dir
```
(main) expert@expert-cws:~/nso-instance-1$ ncs-netsim create-network ~/local-nso/packages/neds/cisco-ios-cli-6.103 1 xe --dir ./netsim
DEVICE xe0 CREATED
```
b) Start netsim
```
(main) expert@expert-cws:~/nso-instance-1$ ncs-netsim start
DEVICE xe0 OK STARTED
```
c) Export simulated devices info to xml file
```
(main) expert@expert-cws:~/nso-instance-1$ ncs-netsim ncs-xml-init > devices.xml
```
d) Load file into NCS
If ncs not started - put file into ncs-cdb. If already started - load file using `ncs_load -l -m devices.xml` command.
e) list netsim devices `ncs-netsim list`
f) To log in into device - use `ncs-netsim cli-c <devicename>`
#TODO: Create dedicated document for ncs-netsim

4. Start ncs and create template
```
admin@ncs(config)# devices template ACL
admin@ncs(config-template-ACL)# ned-id cisco-ios-cli-6.103 
admin@ncs(config-ned-id-cisco-ios-cli-6.103)# config
admin@ncs(config-config)# access-list access-list 10 rule "permit 192.0.2.0 0.0.0.255"
admin@ncs(config-rule-permit 192.0.2.0 0.0.0.255)# top
admin@ncs(config)# show configuration 
devices template ACL
 ned-id cisco-ios-cli-6.103
  config
   access-list access-list 10
    rule "permit 192.0.2.0 0.0.0.255"
    !
   !
  !
 !
!
admin@ncs(config)# commit
```
5. Apply template to device
```
admin@ncs(config)# devices device xe0 
admin@ncs(config-device-xe0)# apply-template template-name ACL
apply-template-result {
    device xe0
    result ok
}
admin@ncs(config-device-xe0)# show configu
devices device xe0
 config
  access-list 10 permit 192.0.2.0 0.0.0.255
 !
!
admin@ncs(config-device-xe0)# commit
Commit complete.
```

https://developer.cisco.com/docs/nso-guides-6.2/#!network-simulator/using-netsim


Clean-up

ncs --stop
rm -rf nso-instance-1
net-stim