# euler 30

# 

power = 5
sum1 = 0
for i in range(2, 1000000):
	if  sum([int(x)**power for x in list(str(i))]) == i:
		sum1 += i
		print(i, sum1)