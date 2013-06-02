# euler 21

def proper_divs(num):
	return [x for x in range(1,num/2+1) if num%x==0]

# sum of divisors of num
def d(num):
	return sum(proper_divs(num))

result = []

for a in range(2,10000):
	b = d(a)
	aa = d(b)
	if a == aa and a != b:
		print(a,b)
		if a not in result:
			result.append(a)
		if b not in result:
			result.append(b)
print('result: ', result, 'sum: ', sum(result))

