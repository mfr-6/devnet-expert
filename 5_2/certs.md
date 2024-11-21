Great resource to understard Certificate management
https://www.feistyduck.com/library/openssl-cookbook/online/

CAUTION: It is not recommended to store private keys in git repository. Although i did that since those will not be user anywhere and i want to have them so i can come back to it later for study purposes.

Key steps:
1. Decide what algorithm you want to use:
    - It could be RSA, DSA, ECDSA, EdDSA. RSA and ECDSA are most used nowadays.
2. Decide what key size you'd like to use:
    - 2048 bit is considered secure for RSA
    - 256 bit is considered secure for ECDSA
3. Passphrase is optional but recommended.
    - Protected key doesn't increase security much, since certs are stored unprotected in program memory so once server is breached, key could be read from memory.



# Cert conversions
https://www.feistyduck.com/library/openssl-cookbook/online/openssl-command-line/key-and-certificate-conversion.html

