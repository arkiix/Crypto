from Crypto.Util.number import long_to_bytes
import owiener

def attack(n, e, c):
    d = owiener.attack(e, n)

    if d == None:
        return d

    dt = pow(c, d, n)
    return long_to_bytes(dt)

print(attack(N, e, c))