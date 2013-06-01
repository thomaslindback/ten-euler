# euler 32
upper_limit = 28123


abundant_numbers = []

def proper_divs(num):
	return [x for x in range(1,num/2+1) if num%x==0]

for i in range(2,28123+1):
	if sum(proper_divs(i)) > i:
		abundant_numbers.append(i)

print(len(abundant_numbers))
print(6965)

all_numbers = [x for x in range(0,28123)]
for i in range(0, len(abundant_numbers)):
	for j in range(i, len(abundant_numbers)):
		 ss = abundant_numbers[i] + abundant_numbers[j]
		 if ss < 28123:
			all_numbers[ss] = 0
			
print(abundant_numbers[0:300])
print(all_numbers[0:300])
print(sum(all_numbers))
print(4179871)
