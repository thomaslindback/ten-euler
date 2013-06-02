# euler 32
# pandigital 1-9

from math import factorial

def li2int2(li):
	return int(''.join(str(i) for i in li))

def li2int3(li):
	return int(''.join(map(str,li)))

def perm(thatone, li):
	if li == []:
		return []
	q,r=divmod(thatone, factorial(len(li)-1))
	tmp = []
	tmp.append(li[q])
	return tmp + perm(r,li[:q] + li[q+1:])

prods = []

def check_pandigital(li):
	for i in range(1, 8):
		for j in range(i+1, 9):
			if li2int2(li[:i]) * li2int2(li[i:j]) == li2int2(li[j:]):
				print(li[:i], li[i:j], li[j:])
				if li2int2(li[j:]) not in prods:
					prods.append(li2int2(li[j:]))


for i in range(0,362800+1):
	check_pandigital(perm(i, [1,2,3,4,5,6,7,8,9]))

print(prods)
print(sum(prods))
#print(check_pandigital(perm(0, [1,2,3,4,5,6,7,8,9])))
#print(perm(1, [1,2,3,4,5,6,7,8,9]))
#print(perm(2, [1,2,3,4,5,6,7,8,9]))


