# euler 34

from math import factorial

lookup_fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
total = 0
for num in range(3,100000):
	lint = [int(x) for x in list(str(num))]
	kk = sum([lookup_fact[i] for i in lint])
	if kk == num:
		print(num, kk)
		total += num
print(total)

