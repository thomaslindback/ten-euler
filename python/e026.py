# euler 26
from math import sqrt, ceil
 
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
 
n = 997
for p in range(n, 1 ,-2):
	if not is_prime(p): continue
	c = 1
	while (pow(10, c) - 1) % p != 0:
		c += 1
	if (p-c) == 1: break

print "Answer to PE26 = ",p

print('------------')
print('the period length of the decimal expansion for a/b is the smallest d >= 1')
print('such that 10^d = 1 mod b')
print('http://www.math.uconn.edu/~kconrad/blurbs/ugradnumthy/eulerthm.pdf')
max_cycle = 0

def report(d, cycle):
	global max_cycle
	
	if cycle > max_cycle:
		max_cycle = cycle
		print(d, max_cycle)

for b in range(6,1000):
	if not is_prime(b):
		continue
	d = 1
	while (pow(10,d)-1) % b != 0:
		d += 1
	report(b,d)