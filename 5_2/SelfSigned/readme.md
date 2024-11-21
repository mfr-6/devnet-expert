# Self-signed certificates
To create self-signed certificate:
```
openssl req -new -x509 -days 365 -key ecdsa-ss.key -out selfsigned1.csr
```
or if you don't have a key, you can generate it along with self-signed cert generation process. (add -nodes to do not encrypt the key)
```
openssl req -nodes -new -newkey rsa:2048 -x509 -days 365 -keyout rsa-ss-new.key -out selfsigned2.csr -subj '/CN=Admin/O=DEVNET CORP/C=PL'
```
To preview generated cert:
```
openssl x509 -text -in selfsinged1.csr -noout
```