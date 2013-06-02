# euler 24
from math import factorial

def perm(n, s):
	if len(s)==1: return s
	q, r = divmod(n, factorial(len(s)-1))
	return s[q] + perm(r, s[:q] + s[q+1:])

print(perm(5,'0123'))
print(perm(999999,'0123456789'))

def perma(thatone, li):
	if li == []:
		return []
	q,r=divmod(thatone, factorial(len(li)-1))
	tmp = []
	tmp.append(li[q])
	return tmp + perma(r,li[:q] + li[q+1:])
	
myres = perma(999999, [0,1,2,3,4,5,6,7,8,9])
print(''.join(str(x) for x in myres))
print(perma(1, [0,1,2,3,4,5,6,7,8,9]))

  