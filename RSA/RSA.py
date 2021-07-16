from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util.number import getPrime

def encrypt(plain):
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q

    e = 2 ** 16 + 1
    phi = (p - 1) * (q - 1)

    d = pow(e, -1, phi)

    c = pow(bytes_to_long(plain.encode()), e, n)

    return c, n, e, d

def decrypt(cipher, n, d):
    dt = pow(cipher, d, n)
    return long_to_bytes(dt).decode()


c, n, e, d = encrypt('Hello, World!')
dt = decrypt(c, n, d)
print(dt)