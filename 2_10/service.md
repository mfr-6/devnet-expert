Service - arbitrary set of configuration templates and variables that can be applied to many network devices. NSO tracks service meaning that when service instance is deleted - NSO removes only related configuration and nothing else.

If something goes wrong in any step of service provisioning, then NSO will revert the configuration to the last good known state (before the last transaction).

Service:
- declarative method to abstract and automate a task you want to do repeatedly
- customer facing and resource facing services
- internally it maintains mapping between inputs (user intent) and outputs (infrastructure configurations)


Service enables us to expose network functionality in an abstracted way - example: VPN S2S (something that needs to be done in multiple places to work, like: s2s tunnel, routing on core routers, firewall policies etc - think of it as end-to-end automation)
ref: https://developer.cisco.com/learning/labs/learn-nso-the-easy-way/nso-services/


### Creating service

1. Go to `packages` directory inside nso instance
2. Create service skeleton
```
ncs-make-package --service-skeleton template <name>
```
3. Make changes to your templates etc.
4. Compile service
  a) Go do (nso-dir)/packages/<service-name>/src
  b) execute `make`
  ```
  (main) expert@expert-cws:~/nso-sbx-nso/packages/loopback-service/src$ make
mkdir -p ../load-dir
/home/expert/local-nso/bin/ncsc `ls loopback-service-ann.yang  > /dev/null 2>&1 && echo "-a loopback-service-ann.yang"` \
	--fail-on-warnings \
	 \
	-c -o ../load-dir/loopback-service.fxs yang/loopback-service.yang
(main) expert@expert-cws:~/nso-sbx-nso/packages/loopback-service/src$ 
```
5. Go to NSO CLI and reload packages using `packages reload` command.

### Configuration template

In order to prepare template, you need to have valid XML data. This can be fetched from device using `commit dry-run outformat xml` once configuring device via NSO.

```
admin@ncs(config)# show configuration 
devices device dist-rtr01
 config
  interface Loopback100
   ip address 10.10.30.0 255.255.255.0
   no shutdown
  exit
 !
!
admin@ncs(config)# commit dry-run outformat xml
result-xml {
    local-node {
        data <devices xmlns="http://tail-f.com/ns/ncs">
               <device>
                 <name>dist-rtr01</name>
                 <config>
                   <interface xmlns="urn:ios">
                     <Loopback>
                       <name>100</name>
                       <ip>
                         <address>
                           <primary>
                             <address>10.10.30.0</address>
                             <mask>255.255.255.0</mask>
                           </primary>
                         </address>
                       </ip>
                     </Loopback>
                   </interface>
                 </config>
               </device>
             </devices>
    }
}
admin@ncs(config)# 
```

### Configuring newly created service
```
admin@ncs(config)# loopback-service test
admin@ncs(config-loopback-service-test)# device dist-rtr01 
admin@ncs(config-loopback-service-test)# dummy 192.168.1.1
admin@ncs(config-loopback-service-test)# top
admin@ncs(config)# commit dry-run outformat native
native {
    device {
        name dist-rtr01
        data interface Loopback100
              ip redirects
              ip address 192.168.1.1 255.255.255.0
              no shutdown
             exit
    }
}
admin@ncs(config)# 
```

### Redeploying service

There might be a case where somebody configured devices and makes changes that are out-out-base changes that NSO is not aware of and it conflicts with service.

0. Simulate config deletetion.
1. Relearn device configuration so NSO is aware about changes deployed out of band.
```
devices sync-from dry-run
devices sync-from
```
2. re-deploy service
```
admin@ncs(config)# loopback-service test re-deploy dry-run 
cli {
    local-node {
        data  devices {
                   device dist-rtr01 {
                       config {
                           interface {
              +                Loopback 100 {
              +                    ip {
              +                        address {
              +                            primary {
              +                                address 192.168.1.1;
              +                                mask 255.255.255.0;
              +                            }
              +                        }
              +                    }
              +                }
                           }
                       }
                   }
               }
              
    }
}
admin@ncs(config)# loopback-service test re-deploy        
admin@ncs(config)# 
```
