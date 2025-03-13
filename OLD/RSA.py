import random
from random import randrange

def is_prime(n):
    if n == 2:
        return True
    if not n & 1:
        return False

    def miller_rabin_test(n, b, s, t):
        x = pow(b, n-1, n)
        if x == 1:
            return True
        for i in range(s - 1):  # Changed xrange to range
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1
    k = s - 1
    for i in range(k):  # Changed xrange to range
        b = randrange(2, n - 1)
        if not miller_rabin_test(n, b, s, d):
            return False
    return True

def mod_exp(a, e, n):
    s = [1]
    r = []
    x = bin(e)
    for k in range(len(x) - 2):
        if int(x[k + 2]) == 1:
            r.append(s[-1] * a % n)
        else:
            r.append(s[-1])
        s.append(r[-1] ** 2 % n)
    return r[-1]

def extended_gcd(a, b):
    d = [a, b]
    s = [1, 0]
    t = [0, 1]
    while d[-1] != 0:
        q = d[-2] // d[-1]
        d.append(d[-2] - q * d[-1])
        s.append(s[-2] - q * s[-1])
        t.append(t[-2] - q * t[-1])
    return (s[-2], t[-2])

def rsa_genkey(key_length):
    primes = []
    p = 1
    q = 2
    e = 3
    m = []

    while len(primes) < 3:
        m.append(randrange(1, 2 ** (key_length - 1), 2))
        if is_prime((2 ** (key_length - 1)) + m[-1]) == True:
            primes.append(2 ** (key_length - 1) + m[-1])

    p = primes[0]
    q = primes[1]
    e = primes[2]
    n = p * q
    d, x = extended_gcd(e, ((p - 1) * (q - 1)))
    d %= (p - 1) * (q - 1)
    pk = n, e
    sk = p, q, d
    return sk, pk

def rsa_encrypt(m, pk):
    n, e = pk
    ct = mod_exp(m, e, n)
    return ct

def rsa_decrypt(ct, sk):
    p, q, d = sk
    m = mod_exp(ct, d, p * q)
    return m

key_length = 20
sk, pk = rsa_genkey(key_length)
m = 1234
ct = rsa_encrypt(m, pk)
n, e = pk
m = rsa_decrypt(ct, sk)

print ("ct", ct)
print ("m", m)
