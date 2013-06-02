# euler 28
# sum of numbers on the diagonals on a 1001 square

size = 1001

sum_diags = 1

for i in range(3,size+1,2):
	sum_diags += sum([i**2-x*(i-1) for x in range(0,4)])

print('answer: ', sum_diags)