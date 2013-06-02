# euler 22

def namepoints(name):
	return sum([(ord(x)-64) for x in name])

names = []
f = open('euler/names22.txt', 'r')
for i, line in enumerate(f):
	line = line.rstrip()
	line = line.replace('"','')
	names = line[:].split(',')

names.sort()
total_sum = 0
for i, n in enumerate(names):
	nsum = namepoints(n)
	total_sum += (i+1)*nsum
	print(i+1, n, nsum, (i+1)*nsum, total_sum)

print('total_sum: ', total_sum)
f.close()
	