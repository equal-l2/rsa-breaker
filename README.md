# rsa-breaker
Reconstruct the corresponding RSA private key from a RSA public key (both in PEM format).
(Only work for very short keys)

Implementations:
- [x] Python
- [ ] Rust
- [ ] Go

## Logic
All programs runs under the same logic as shown bellow.
1. Read a RSA public key in PEM.
2. Extract the modulus.
3. Factorize the modulus and get primes.
4. Calculate parameters for the private key.
5. Reconstruct the private key from the parameters and output in PEM.
