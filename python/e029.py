# euler 29

ss  = set()
#[ss.add(2**i) for i in range(2,101)]
#print(len(ss))
#[ss.add(4**i) for i in range(2,101)]
#print(len(ss))
#[ss.add(16**i) for i in range(2,101)]
#print(len(ss))

sum_unique = 0 
for i in range(2,101):
	[ss.add(i**j) for j in range(2,101)]
print('sum', len(ss))
