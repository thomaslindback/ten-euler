# euler 67

dic = {}

f = open('euler/triangle67.txt', 'r')
for i, line in enumerate(f):
	line = line.rstrip()
	dic[i+1] = map(int, line[:].split(' '))

n =len(dic)
for i in range(n-1,0,-1):
	row = dic[i]
	next = dic[i+1]
	for idx, val in enumerate(row):
		row[idx] += max(next[idx],next[idx+1])
print(dic[1])
