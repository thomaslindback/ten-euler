# Project Euler 2

def fib(n):
	a,b = 1,2
	for _ in xrange(n):
		res = a + b
		yield res
		a, b = b, res

sum = 2
for i in fib(1000):
	if i > 4000000:
		break
	elif i % 2 == 0:
			sum += i

print sum
