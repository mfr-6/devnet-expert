# NSO

- `System Install` - "always-on" production grade NSO instance.
- `Local Install` - used for development and evaluation purposes. 

It's important to source `ncsrc` every time when logged in to NSO host.

## Setting up NCS with NEDs

```
ncs-setup \
--package <path to NED1> \
--package <path to NED2> \
--dest nso-instance
```

### NCS Instance
In created dir using `ncs-setup` command, you can find:
- `ncs.conf` - Configuration file used to customize aspects of the NSO instance
- `packages/` - Directory that contains symlinks to specified NEDs during setup
- `logs/` - all logs from NSO

To start NCS instance, simply execute `ncs` command in instance directory. To verify service status, use `ncs --status | grep status`.

To enter NSO instance, use `ncs_cli -C -u admin`. `-C` stands for 'Cisco-style' command line (default is Juniper style)

### Device authgroup
TODO:

### Adding device to NSO
```
set devices device edge-sw01 address 10.10.20.172 authgroup labadmin device-type cli ned-id cisco-ios-cli-6.91 protocol telnet
set devices device edge-sw01 address 10.10.20.172 ssh host-key-verification none
commit
```

### Connecting to device
When in config context of selected device, you can issue `connect` to see if NSO is able to connect to device.
```
admin@ncs(config)# devices device edge-sw01 
admin@ncs(config-device-edge-sw01)# connect
result false
info Device edge-sw01 is southbound locked
admin@ncs(config-device-edge-sw01)# 
```

But NSO's default mode for devices is a locked. This is to prevent NSO from interacting with device until administrator is ready. We can disable this maintenance state by adding `state admin-state unlocked` configuration.

### Adding devices into NSO
You can add devices via:
- Manually
- RESTAPI
- `load merge` - inject data from other NSO to local instance.

### Grouping devices
```
devices device-group <name>
device-name <device-name>
device-group <group-name>
```

### Check sync
It's possible to see if any out-of-band changes took place that NSO is not aware
```
devices device-group <group-name> check-sync
```

### Configuring single device
1. Enter to configuration context of specific device
`devices device <device-name>`
2. Issue `config` to start configuring device
```
admin@ncs(config)# devices device dist-sw01
admin@ncs(config-device-dist-sw01)# config
admin@ncs(config-config)# 
```
3. Preview configuration:
```
admin@ncs(config)# show configuration 
devices device dist-sw01
 config
  vlan 42
   name Test
  exit
  interface Vlan42
   no shutdown
   description This is config created in NSO
   ip address 10.42.42.42/24
  exit
 !
!
```
4. Execute `dry-run` to see what NSO will send to device
```
admin@ncs(config)# commit dry-run outformat native
native {
    device {
        name dist-sw01
        data vlan 42
              name Test
             exit
             interface Vlan42
              no shutdown
              description This is config created in NSO
              ip address 10.42.42.42/24
             exit
    }
}
```

### Roll back configuration
- NSO stores configuration rollbacks for every change.
- Each commit is a rollback, which means that if you'll configure 10 devices in a single commit, you'll revert those changes with rollback

1. Preview what will be issued at rollback
```
admin@ncs(config)# show configuration rollback changes
devices device dist-sw01
 config
  no vlan 42
  no interface Vlan42
 !
!
```
2. Execute `rollback configuration` to prepare configuration into a staging area.
3. Use `commit dry-run outformat native` to see what NSO will do when config is commited.
```
admin@ncs(config)# commit dry-run outformat native
native {
    device {
        name dist-sw01
        data no vlan 42
             no interface Vlan42
    }
}
```
4. Perform rollback with `commit`.

### Configuration templates
1. Go to `devices template` context 
2. Select NED for template
3. Prepare configuration
```
admin@ncs(config)# devices template SET-DNS-SERVER
admin@ncs(config-template-SET-DNS-SERVER)# ned-id cisco-nx-cli-5.23 
adnfigncs(config-ned-id-cisco-nx-cli-5.23)# conf
admin@ncs(config-config)# ip name-server servers 208.67.222.222
admin@ncs(config-config)# ip name-server servers 208.67.220.220
admin@ncs(config-config)# top
admin@ncs(config)# show config
devices template SET-DNS-SERVER
 ned-id cisco-nx-cli-5.23
  config
   ip name-server servers [ 208.67.222.222 208.67.220.220 ]
  !
 !
!
```
4. Apply configuration to devices
```
admin@ncs(config)# devices device dist-sw01 apply-template template-name SET-DNS-SERVER 
apply-template-result {
    device dist-sw01
    result ok
}
```

It's possible to prepare the same configuration for different platforms thanks to NEDs
```
devices template SET-DNS-SERVER
! IOS TEMPLATE
ned-id cisco-ios-cli-6.91
config
ip name-server name-server-list 208.67.222.222
ip name-server name-server-list 208.67.220.220
exit
exit
exit

! ASA TEMPLATE
! 3 exits to return back to the 'config-template-SET-DNS-SERVER' context
ned-id cisco-asa-cli-6.6
config
dns domain-lookup mgmt
dns server-group DefaultDNS
name-server 208.67.220.220
name-server 208.67.222.222
exit
exit
exit

! IOS-XR TEMPLATE
ned-id cisco-iosxr-cli-7.45
config
domain name-server 208.67.222.222
exit
domain name-server 208.67.220.220
```

### Useful commands:
- `pwd` - preview the config context you are in
- `show devices list` - display all configured devices
- `load merge <path>` - load configuration from text file
- `devices sync-from` - learn current config of managed devices
- `show running-config devices device <device-name> config` - show configuration for specified device from NSO's CDB.
- `show running-config devices device <device-name> | de-select config` - display info about device excluding config from CDB
- `show running-config devices device <device-name> | display json` - display data in json format
- `show running-config devices device <device-name> config interface Vlan * ip address` - show `ip address` section across all Vlan interfaces on a device
- `show configuration | display xml` - preview configuration not yet commited in xml format.
- `revert` - discard not commited configuration
- `commit dry-run outformat native` - perform dry-run for prepared configuration
- `show running-config devices device <device-name> config | display xpath` - display xpath specific for particular device config
```
admin@ncs# paginate false
admin@ncs# show running-config devices device netsim-ios config | display xpath
/devices/device[name='netsim-ios']/config/ios:tailfned/device netsim
/devices/device[name='netsim-ios']/config/ios:tailfned/police cirmode
/devices/device[name='netsim-ios']/config/ios:ip/source-route true
/devices/device[name='netsim-ios']/config/ios:ip/vrf[name='my-forward']/bgp/next-hop/Loopback 1
/devices/device[name='netsim-ios']/config/ios:ip/http/server false
/devices/device[name='netsim-ios']/config/ios:ip/http/secure-server false
```

### Gathering data from devices
- `show devices device <device-name> platform` - get platform information from device
- `show devices device <device-name> live-status ip route` - `live-status` is used to read from the device at the time of execution.
- `devices device <device-name> live-status exec <command>` - execute command on remote device
- `devices device <device-name> live-status exec <command> | save /home/developer/...` - execute command on remote device and save the output to a file

```
show devices device dist-sw01 platform
platform name NX-OS
platform version 9.3(8)
platform model "cisco Nexus9000 C9300v Chassis "
platform serial-number 9QF63L920NR
admin@ncs# show devices device dist-sw01 platform model
platform model "cisco Nexus9000 C9300v Chassis "
admin@ncs# show devices device dist-sw01 platform serial-number
platform serial-number 9QF63L920NR

admin@ncs# show devices device * platform serial-number
                SERIAL       
NAME            NUMBER       
-----------------------------
core-rtr01      33AA3ADE9EE  
core-rtr02      BEB192EB242  
dist-rtr01      93X4XLANMYG  
dist-rtr02      9MBTPFN17MJ  
dist-sw01       9QF63L920NR  
dist-sw02       9OA0UP11SVC  
edge-sw01       9MH1LBYODF6  
internet-rtr01  9GYLKKRUY7W  
```
Live-status
```
admin@ncs# show devices device dist-sw01 live-status ip route
                              UCAST  MCAST                                                                                 
NAME        IPPREFIX          NHOPS  NHOPS  ATTACHED  IPNEXTHOP     UPTIME       IFNAME   PREF  METRIC  CLIENTNAME  UBEST  
---------------------------------------------------------------------------------------------------------------------------
default     172.16.101.0/24   1      0      true      172.16.101.2  PT4H44M22S   Vlan101  0     0       direct      true   
            172.16.101.1/32   1      0      true      172.16.101.1  PT4H44M1S    Vlan101  0     0       hsrp        true   
            172.16.101.2/32   1      0      true      172.16.101.2  PT4H44M22S   Vlan101  0     0       local       true   
            172.16.252.0/30   1      0      true      172.16.252.1  PT4H44M23S   Eth1/3   0     0       direct      true   
            172.16.252.1/32   1      0      true      172.16.252.1  PT4H44M23S   Eth1/3   0     0       local       true   
            172.16.252.12/30  1      0      false     172.16.252.6  PT4H44M15S   Eth1/4   110   41      ospf-1      true   
            172.16.252.16/30  2      0      false     172.16.252.2  PT4H44M15S   Eth1/3   110   41      ospf-1      true   
                                                      172.16.252.6  PT4H44M15S   Eth1/4   110   41      ospf-1      true   
            172.16.252.20/30  1      0      false     172.16.252.2  PT4H44M15S   Eth1/3   110   41      ospf-1      true   
            172.16.252.24/30  1      0      false     172.16.252.2  PT4H44M15S   Eth1/3   110   41      ospf-1      true   
            172.16.252.28/30  1      0      false     172.16.252.6  PT4H44M15S   Eth1/4   110   41      ospf-1      true   
            172.16.252.32/30  1      0      false     172.16.252.6  PT4H44M15S   Eth1/4   110   41      ospf-1      true   
            172.16.252.4/30   1      0      true      172.16.252.5  PT4H44M23S   Eth1/4   0     0       direct      true   
            172.16.252.5/32   1      0      true      172.16.252.5  PT4H44M23S   Eth1/4   0     0       local       true   
            172.16.252.8/30   1      0      false     172.16.252.2  PT4H44M15S   Eth1/3   110   41      ospf-1      true   
management  0.0.0.0/0         1      0      false     10.10.20.254  PT12H16M50S  -        1     0       static      true   
            10.10.20.0/24     1      0      true      10.10.20.177  PT12H16M51S  mgmt0    0     0       direct      true   
            10.10.20.177/32   1      0      true      10.10.20.177  PT12H16M51S  mgmt0    0     0       local       true  
```

# Sandbox recommended labs:

- Get started with NSO: https://developer.cisco.com/learning/tracks/get_started_with_nso/
- Sandbox: Network Services Orchestrator

### Command used in Sandbox
Commands pasted below for my comfort to reuse them later

```
ncs-setup --package nso/packages/neds/cisco-nx-cli-5.23 --package nso/packages/neds/cisco-asa-cli-6.6 --package nso/packages/neds/cisco-ios-cli-6.91 --package nso/packages/neds/cisco-iosxr-cli-7.45 --dest nso-instance
```

- `ncs` - start NCS service
- `ncs --stop` - stop NCS service
- `ncs --status | grep status` - show NCS service status

### ncs-netsim

# TODO:

NCS Netsim is a NCS utility to simulate network devices. NED is required to simulate device

```
ncs-netsim --dir ~/src/netsim create-device $NCS_DIR/packages/neds/cisco-ios-cli-3.8 netsim-ios
ncs-setup --dest ~/src --netsim-dir ~/src/netsim
cd ~/src
ncs-netsim start
ncs
ncs_cli -C -u admin
```
ncs-netsim --dir ~/src/netsim create-device $NCS_DIR/packages/neds/cisco-ios-cli-3.8 netsim-ios

or 

ncs-netsim --dir ~/src/nso-instance/netsim create-network $NCS_DIR/packages/neds/cisco-ios-cli-3.0 2 dist-rtr
ncs-netsim --dir ~/src/nso-instance/netsim add-to-network $NCS_DIR/packages/neds/cisco-ios-cli-3.0 1 edge-sw
ncs-netsim --dir ~/src/nso-instance/netsim add-to-network $NCS_DIR/packages/neds/cisco-ios-cli-3.0 1 internet-rtr
ncs-netsim --dir ~/src/nso-instance/netsim add-to-network $NCS_DIR/packages/neds/cisco-iosxr-cli-3.5 2 core-rtr
ncs-netsim --dir ~/src/nso-instance/netsim add-to-network $NCS_DIR/packages/neds/cisco-nx-cli-3.0 2 dist-sw
ncs-netsim --dir ~/src/nso-instance/netsim add-to-network $NCS_DIR/packages/neds/cisco-asa-cli-6.6 1 edge-firewall


(main) expert@expert-cws:~/netsim-1$ cd ..
(main) expert@expert-cws:~$ ncs-setup --dest ~/nso-netsim --netsim-dir ~/netsim-1/ 
Using netsim dir /home/expert/netsim-1/
(main) expert@expert-cws:~$ cd nso-netsim/
(main) expert@expert-cws:~/nso-netsim$ ncs
(main) expert@expert-cws:~/nso-netsim$ ncs_cli -C -u admin

admin connected from 127.0.0.1 using console on expert-cws
admin@ncs# show devices list
NAME       ADDRESS    DESCRIPTION  NED ID               ADMIN STATE  
-------------------------------------------------------------------
dist-rtr0  127.0.0.1  -            cisco-ios-cli-6.103  unlocked     
dist-rtr1  127.0.0.1  -            cisco-ios-cli-6.103  unlocked     
admin@ncs# 

admin@ncs(config)# commit            
Aborted: Failed to connect to device dist-rtr0: connection refused: NEDCOM CONNECT: Connection refused in new state