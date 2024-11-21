
# Cert valid for multiple hostnames
We can set subjectAltName to support multiple hostnames
Extention file: example.ext
```
openssl x509 -req -days 365 -in cert1.csr -signkey ecdsa.key -out cert3.crt -extfile example.ext
```
