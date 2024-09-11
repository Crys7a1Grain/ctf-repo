from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import getPrime

PRIME_LENGTH = 24
NUM_PRIMES = 256

FLAG = b"gctf{redacted}" #строка в байтах

N = 1
e = 65537

for i in range(NUM_PRIMES): #i: 0 -> 256
    prime = getPrime(PRIME_LENGTH) #[2,24]
    N *= prime

ct = pow(bytes_to_long(FLAG), e, N)

# ct = bytes_to_long(FLAG) ** e % N

# a = x + b * c

# print(f"{N=}")
# print(f"{e=}")
# print(f"{ct=}")

print(bytes_to_long(b"123"))