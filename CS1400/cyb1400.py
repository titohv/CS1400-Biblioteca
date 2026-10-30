"""
Title: rsa_encrypt.py
Author: Lance P. Rhodes
Description: Program to demonstrate asymmetric encryption using the Rivest-Shamir-
Adleman (RSA) algorithm. The algorithm employs the properties of large prime
numbers to generate public and private keys. The public key is used to encrypt
data, but only the private key can be used to decrypt it. A select few, low-value
prime numbers are hard-coded into the program for simplicity. In practice, prime
numbers should result in a minimum key length of 2048 bits, or an integer that is
approximately 2^1024 - 1 for each of the prime numbers p and q.
"""
import random
import math
# Returns the modular multiplicative inverse (b) given (a, m) such that:
# (a x b) % m = 1
def mod_inverse(a, m):
b = 0
while (a * b) % m != 1:
b += 1
return b
# Returns a random coprime number, given (n)
def random_coprime(n):
while True:
c = random.randint(2, n - 1)
if math.gcd(c, n) == 1:
return c
def generate_rsa_key():
# Select two distinct random prime numbers: p, q.
primes = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
151, 157, 163, 167, 173, 179, 181, 191, 193, 197]
p = random.choice(primes)
primes.remove(p)
q = random.choice(primes)
# Compute Euler's totient function: phi_n.
phi_n = (p - 1) * (q - 1)
# Select a random coprime between 1 and phi_n; e used for public key.
e = random_coprime(phi_n)
# Modular multiplicative inverse of e; d used for private key.
d = mod_inverse(e, phi_n)
# Calculate the product of p and q, used by public/private keys.
n = p * q
return {'n': n, 'public': e, 'private': d}
def parse_key(access):
while True:
k = (input(f'Enter {access} key in the format n, e: ')
.replace(' ', ''))
if ',' in k and k.replace(',', '').isdigit():
mod = int(k[:k.find(',')])
exp = int(k[k.find(',') + 1:])
return [mod, exp]
else:
print('Invalid key')
print('Rhodes Asymmetric RSA Key Generator/Tester')
while True:
select = input('\n1 - Generate Random RSA Key\n2 - Encrypt\n'
'3 - Decrypt\n4 - Exit\n\nSelection: ')
if select == '1':
key = generate_rsa_key()
print(f'Public key: {key["n"]}, {key["public"]}')
print(f'Private key: {key["n"]}, {key["private"]}')
elif select == '2':
data_string = input('Enter data string: ')
key = parse_key('public')
encrypted_data = [(ord(i)**key[1] % key[0]) for i in data_string]
print('Encrypted data:', encrypted_data)
elif select == '3':
while True:
data_string = input('Enter encrypted data points, '
'comma separated: ').replace(' ', '')
if data_string.replace(',', '').isdigit():
break
print('Invalid data entry.')
data_points = data_string.split(',')
key = parse_key('private')
print('Decrypted data:', end=' ')
for point in data_points:
print(chr(int(point)**key[1] % key[0]), end='')
print()
elif select == '4':
break