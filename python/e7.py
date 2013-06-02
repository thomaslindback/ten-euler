# Project Euler 7

from math import sqrt

def is_prime(cand):
	if cand < 2 or cand%2 == 0 or cand%3 == 0: return False
	limit = sqrt(cand) + 1
	d = 3
	while d <= limit:
		if  cand%d == 0:
			return False
		d += 2
	return True


i, numbers_of_prime = 5, 2
while numbers_of_prime != 10001:
	if is_prime(i):
		numbers_of_prime += 1
		res = i
	i += 2

print res, numbers_of_prime
