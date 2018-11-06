#!/usr/bin/env python3
from Cryptodome.PublicKey import RSA
from sympy.ntheory import primefactors
from sympy.core.numbers import mod_inverse
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <RSA public key PEM>")
    sys.exit(1)

# Read the public key
print("Reading the public key")
with open(sys.argv[1], 'r') as f:
    pubkey = RSA.import_key(f.read())

# Is the read key really a public key?
if pubkey.has_private():
    print("The passed key is a private key")
    sys.exit(1)

# Factorize the modulus (the most ridiculous part!)
modulus = pubkey.n
print("Factorizing (It takes years :( ) ")
l = primefactors(modulus)
print("Done :)")

# Generate private key from the factors
print("Generating the private key")
prime1 = l[1]  # prime1 > prime2
prime2 = l[0]
public_exp = pubkey.e
private_exp = mod_inverse(public_exp, (prime1-1)*(prime2-1))
# coef = Integer(prime2).invert(prime1)
# print(f"modulus: {prime1 * prime2}")
# print(f"publicExponent: {public_exp}");
# print(f"privateExponent: {private_exp}");
# print(f"prime1: {prime1}");
# print(f"prime2: {prime2}");
# print(f"coefficient: {coef}");
key_components = (pubkey.n, public_exp, private_exp, prime1, prime2)  # , coef)
prikey = RSA.construct(key_components)

# Write the generated private key
outfilename = f"{sys.argv[1]}.out.pem"
print(f"Writing the private key to {outfilename}")
with open(outfilename, 'wb') as f:
    f.write(prikey.export_key('PEM'))
    f.write(b'\n')  # PEMs from OpenSSL have a newline on the end of the file
