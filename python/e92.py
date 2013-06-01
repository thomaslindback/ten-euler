cache = [0]*568
 
for cxi in range(2,568):
  n = cxi
  while n!=1:
    n = sum(int(t)**2 for t in str(n))
    if n==89 or n==4:
      cache[cxi]=1
      break
 
c = 0
for i in range(1,10000000):
  n = sum(int(t)**2 for t in str(i))
  if cache[n]==1: c+=1
 
print "Answer to PE92 = ",c
