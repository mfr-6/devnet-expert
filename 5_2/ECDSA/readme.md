# ECDSA

In ECDSA, key size is controlled by named curve.

Generate key
```
openssl genpkey -out ecdsa.key -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -aes-128-cbc
```

To preview output in readable format, use:
```
openssl pkey -in ecdsa.key -text -noout
```
To generate public part of a key separately
```
openssl pkey -in ecdsa.key -pubout -out pubkey-ecdsa.pub
```