# I cannot login to NSO GUI !!!!

Please log in to your NSO with `ncs_cli` and see if there is "aaa" section in your running-config. If not - that's the reason. Default credentials for local-install are `admin/admin`.

In my case - I ignored error when executing `ncs` command. Previously I've provided multiple NEDs, including ASA one when executing `ncs-setup`. 

```
(main) expert@expert-cws:~/nso-sbx-nso$ ncs
NCS package upgrade failed with reason 'User java class "com.tailf.packages.ned.asa.UpgradeNedSettings" exited with status 1'
Daemon died status=13
```

I thought it was not that important and I agree that my ASA NED might behave not as expected so I executed `ncs` again and service started, but I was not able to log in. I checked running-config and it turned out that default configuration is incomplete. After that I've decided to setup instance from the scratch with `ncs-setup` without ASA NED and then there was no issues when starting ncs service. I reviewed running-config again and i've noticed there is "aaa" section with default "admin" account. I verified access to GUI and I was able to successfully log in. Seems like newest version of ASA NED is not working as expected on CWS. This is something I'll try to investigate later why is that.

# I cannot connect to device - device does not have a Network Element Driver registered
```
admin@ncs(config-device-core-rtr01)# connect
result false
info Device core-rtr01 does not have a Network Element Driver registered
```

1. Check status for packages
```
admin@ncs# show packages package oper-status 
packages package cisco-ios-cli-6.103
 oper-status java-uninitialized
packages package cisco-iosxr-cli-7.53
 oper-status java-uninitialized
packages package cisco-nx-cli-5.25
 oper-status java-uninitialized
admin@ncs# 
```

In above case java is uninitialized - check status for java-vm.
```
admin@ncs# show java-vm status
java-vm status not-connected
```

Check for java-vm logs in logs dir:

In my case - there was a problem with incompatibility (CWS has older Java Runtime which does not meet minimum requirements for Java VM used in NSO 6.2)
```
Starting java-vm with options:
' -classpath :/home/expert/local-nso/java/jar/* -Dhost=127.0.0.1 -Dport=4569 -Djvm.restart.enabled=false -Djvm.restart.errCount=3 -Djvm.restart.duration=60 -Djava.security.egd=file:/dev/./urandom -Dfile.encoding=UTF-8 -Dorg.apache.logging.log4j.simplelog.StatusLogger.level=OFF'
Error: LinkageError occurred while loading main class com.tailf.ncs.NcsJVMLauncher
        java.lang.UnsupportedClassVersionError: com/tailf/ncs/NcsJVMLauncher has been compiled by a more recent version of the Java Runtime (class file version 61.0), this version of the Java Runtime only recognizes class file versions up to 55.0
```

I suggest to upgrade java on CWS, because there is no option to download freetrial of NSO 5.5 that is used in a LAB exam, so eventually you need to stick to 6.2 which is the only one available now.

To have this working you need:
1. Upgrade java - i selected v21

2. Stop NCS service
```
ncs --stop
```
3. Start service and verify if Java VM is up an running
```
admin@ncs# show java-vm status
java-vm status running
```
4. Check if your NEDs are available now:
```
admin@ncs# show packages package oper-status 
                                                                                                        PACKAGE                          
                          PROGRAM                                                                       META     FILE                    
                          CODE     JAVA           PYTHON         BAD NCS  PACKAGE  PACKAGE  CIRCULAR    DATA     LOAD   ERROR            
NAME                  UP  ERROR    UNINITIALIZED  UNINITIALIZED  VERSION  NAME     VERSION  DEPENDENCY  ERROR    ERROR  INFO   WARNINGS  
-----------------------------------------------------------------------------------------------------------------------------------------
cisco-ios-cli-6.103   X   -        -              -              -        -        -        -           -        -      -      -         
cisco-iosxr-cli-7.53  X   -        -              -              -        -        -        -           -        -      -      -         
cisco-nx-cli-5.25     X   -        -              -              -        -        -        -           -        -      -      -         
```

5. Try to connect to device
```
admin@ncs(config)# devices device core-rtr01
admin@ncs(config-device-core-rtr01)# connect
result true
info (admin) Connected to core-rtr01 - 10.10.20.173:23
```