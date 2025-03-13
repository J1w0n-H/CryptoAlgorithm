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

input=[561,569,2 ** (2 ** 4) + 1,2 ** (2 ** 10) + 1,2 ** 1279 - 1,2 ** 2203 - 1,2 ** 3217 - 1]
for i in range(0,7):
	if is_prime(input[i])==True:
		print("y")
	else:
		print("n")
