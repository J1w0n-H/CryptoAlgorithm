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
		for i in xrange(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1
	k=s-1
	for i in xrange(k):
		b = randrange(2, n - 1)
		if not miller_rabin_test(n, b, s, d):
			return False
	return True

def mod_exp(a,e,n):
    s=[1]
    r=[]
    x=bin(e)
    for k in range(len(x)-2):
        if(int(x[k+2])==1):
            r.append(s[-1]*a%n)
        else:
            r.append(s[-1])
        s.append(r[-1]**2%n)
    return r[-1]
'''
def is_prime(n):
    if n <= 1:
        return False
    if mod_exp(n % 2 is 0 or n % 3 is 0:
        return False
    if n <= 3:
        return True
    k, l = 5, n**0.5
    while k <= l:
        if n % k is 0 or n % (k+2) is 0:
            return False
        k += 6
    return True
'''
def extended_gcd(a, b):
    d = [a, b]
    s = [1, 0]
    t = [0, 1]
    while d[-1] != 0:
        q=d[-2]//d[-1]
        d.append(d[-2] -q * d[-1])
        s.append(s[-2] -q * s[-1])
        t.append(t[-2] -q * t[-1])
    return (s[-2], t[-2])


'''
Implement the RSA algorithm by using python. When you submit, you should submit a report file (rsa.pdf) and a souce file (rsa.py). The report file should contain a source code and the running results of your functions in the python shell. The python source file should contain the souce code of your functions.
1) rsa_genkey(key_length): it takes a key bit length and returns a private key sk and a public key pk.
2) rsa_encrypt(m, pk): it takes a message m and returns an encrypted ciphertext ct by using the public key pk.
3) rsa_decrypt(ct, sk): it takes a ciphertext ct and a private eky sk and outputs a decrypted plaintext m by using the private key sk.
The report should contain the results of the following examples for each key_length = 256, 512, and 1024:
>> key_length = 1024
>> sk, pk = rsa_genkey(key_length) 
>> m = 1234
>> ct = rsa_encrypt(m, pk)
>> m = rsa_decrypt(ct, sk)
'''
def mod_exp(a,e,n):
    s=[1]
    r=[]
    x=bin(e)
    for k in range(len(x)-2):
        if(int(x[k+2])==1):
            r.append(s[-1]*a%n)
        else:
            r.append(s[-1])
        s.append(r[-1]**2%n)
    return r[-1]

def rsa_genkey(key_length):

    primes = []
    p=1
    q=2
    e=3
    m=[]


    while len(primes)<3:
        m.append(randrange(1, 2 ** (key_length - 1), 2))
        if is_prime((2**(key_length-1))+m[-1])==True:
            primes.append(2**(key_length-1)+m[-1])


    p=primes[0]
    q=primes[1]
    e=primes[2]
    n=p*q
    d,x=extended_gcd(e,((p-1)*(q-1)))
    d%=(p-1)*(q-1)
    pk=n,e
    sk=p,q,d
    return sk,pk

def rsa_encrypt(m, pk):
    n,e=pk
    ct=mod_exp(m,e,n)
    return ct


def rsa_decrypt(ct, sk):
    p,q,d=sk
    m=mod_exp(ct,d,p*q)
    return m

key_length = 20
sk, pk = rsa_genkey(key_length)
m = 1234
ct = rsa_encrypt(m, pk)
n,e=pk
m = rsa_decrypt(ct, sk)

print ("ct",ct)

print ("m",m)
