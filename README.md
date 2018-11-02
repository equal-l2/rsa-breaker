# rsa-breaker
Reconstruct the corresponding RSA private key from a RSA public key (both in PEM format).  
(Only work for very short keys)

Implementations:
- [x] Python
- [ ] Rust
- [ ] Go

## Logic
All programs runs under the same logic as shown bellow.
1. Read a RSA public key from a PEM and extract the parameters.
2. Factorize the modulus and get primes.
3. Prepare parameters for the private key.  
(Reuse public exponent and modulus, calculate the other parameters)
4. Reconstruct the private key from the parameters and output in PEM.
