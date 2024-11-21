# Certificate Signing Requests (CSR)

Once you have priv key, you can proceed with CSR
```
openssl req -new -key ecdsa-csr.key -out csr1.csr
```
To preview CSR
```
openssl req -text -in csr1.csr -noout
```
It's possible to generate CSR from existing cert to do not repeat all the data like Subjet, Organization name etc
To test it - download cert from website you like and then use it as a reference cert
```
openssl x509 -x509toreq -in <certname> -out csr-x.csr -signkey ecdsa-csr.key 
```

We can also create CSR based on configuration file (example.cnf)
```
openssl req -new -config example.cnf -key ecdsa.key -out ecdsa.csr
```
