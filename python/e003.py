# Project Euler 3

import itertools
from math import sqrt

def erat2( ): # from python cookbook
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

n = 600851475143
lim = sqrt(n)

prims = []
for i in erat2():
	if i > lim:
		break
	elif n%i == 0:
		prims.append(i)

import operator
prod = reduce(operator.mul, prims, 1)

print 'Prims: ', prims, '. Prod is equal to n:', prod == n

	