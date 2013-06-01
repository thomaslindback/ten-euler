# euler 27

# If p(x) is prime-generating for 0<=x<=n, then so is p(n-x).
# 36*n^2 -810n+2753 -> 45
#http://mathworld.wolfram.com/Prime-GeneratingPolynomial.html

from math import sqrt

def euler_sieve(n):
	candidates = range(n+1)
	fin = int(n**0.5)
	for i in xrange(2, fin+1):
		if not candidates[i]:
			continue
		candidates[2*i::i] = [None] * (n//i - 1)
	return [i for i in candidates[2:] if i]

prims = euler_sieve(1000)
print(euler_sieve(1000))

def is_prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(sqrt(n))
	f = 5
	while f <= r:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True

# n^2 + an + b
max_length = 0

for b in prims:
	for a in range(-999, 1000):
		n = 0
		while is_prime(n**2 + a * n + b) == True:
			n += 1
		if n > max_length:
			max_length = n
			max_a = a
			max_b = b

print(max_length, max_a, max_b, max_a*max_b)

