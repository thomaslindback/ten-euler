#euler14

def calc_len(n):
	len = 1
	while n != 1:
		if n%2 == 0:
			n = n/2
		else:
			n = 3*n+1
		len += 1
	return len

max_len = 0
def report(i, r):
	global max_len
	if r > max_len:
		max_len = r
		print(i, max_len)

for i in xrange(1, 1000000):
	report(i, calc_len(i))
