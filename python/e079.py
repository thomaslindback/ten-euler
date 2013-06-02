# euler79

rows = []
f = open('euler/keylog79.txt', 'r')
for line in f:
	line = line.rstrip()
	rows.append(list(line))
	
f.close()

print(rows)
print(len(rows))

dic = {}
for i in [0,1,2,3,6,7,8,9]:
	dic[i] = []
	for row in rows:
		if str(i) in row:
			if row.index(str(i)) == 0:
				if row[1] not in dic[i]:
					dic[i].append(row[1])
				if row[2] not in dic[i]:
					dic[i].append(row[2])
			if row.index(str(i)) == 1:
				if row[2] not in dic[i]:
					dic[i].append(row[2])

for i in [0,1,2,3,6,7,8,9]:
	print(i, len(dic[i]), dic[i])

rsl =[x[0] for x in sorted(dic.iteritems(), key=lambda r: len(r[1]), reverse=True)]
print(''.join(map(str,rsl)))

