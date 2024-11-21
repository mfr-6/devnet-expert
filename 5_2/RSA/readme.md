To generate RSA key, use 'genpkey' command
```
openssl genpkey -out rsakey.key -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -aes-128-cbc

-out -> output filename
-algorithm -> type of algorithm we would like to use
-pkeyopt -> set key-generation-options (can be found under "man openssl-genpkey")
-cipher (-aes-128-cbc in above command) -> Encrypts priv key with supplied cipher (openssl ciphers -s) #TODO: List of supported ciphers

```

To preview output in readable format, use:
```
openssl pkey -in rsa.key -text -noout
```
To generate public part of a key separately
```
openssl pkey -in rsa.key -pubout -out pubkey-rsa.pub
```