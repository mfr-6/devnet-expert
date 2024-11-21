My postman collection for RESTCONF is available here: https://www.postman.com/mfr-6



1. When key of a list is a string that contains slash, i.e "10.1.1.1/32", then in Url you need to provide `%2F`
`https://{{host}}/restconf/data/Cisco-NX-OS-device:System/ipv4-items/inst-items/dom-items/Dom-list=default/rt-items/Route-list=10.10.10.10%2F32`

For IOS-XE it's useful to format config in NETCONF and RESTCONF
`show run | format restconf-json`
`show run | format netconf-xml`