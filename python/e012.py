# euler 12
from operator import mul

def next_comp(n):
	if n%2==0:
		return 2
	for i in range(3, 1+n,2):
		if n%i == 0:
			return i
	return -1

def calc_comps(num, comps):
	while True:
		c = next_comp(num)
		if c != -1:
			comps[c]+=1
			num = num/c
		else:
			break

def gettri(num):
	return (num+1)*num/2

for t in range(2, 25000):
	comps = [0]*15000
	tr = gettri(t)
	if t%2 == 0:
		calc_comps(tr/(t+1), comps)
		calc_comps(t+1, comps)
	else:
		calc_comps(tr/t, comps)
		calc_comps(t, comps)
	pows = [i+1 for i in comps if i > 0]
	divs = reduce(mul,pows)
	print('tr no:', t, 'tr: ', tr, 'number of d:', divs)
	if divs > 500:
		print('tr no:', t, 'tr: ', tr, 'number of d:', divs)
		break


