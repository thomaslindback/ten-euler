from fractions import gcd 

def lcm(a,b):
	return a*b/gcd(a,b)

def check(res, myrange):
	return all([res%i==0 for i in myrange])

ran = range(20,1,-1)
result = ran[0]
for i in ran:
	result = lcm(result,i)
	print(result, i)


