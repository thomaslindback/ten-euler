# Project Euler 5

from fractions import gcd 

def lcm(a,b):
	return a*b/gcd(a,b)

def check(res, myrange):
	return all([res%i==0 for i in myrange])

res = reduce(lambda x, y: lcm(y,x), range(1, 21))
print res, check(res, range(1, 21))
