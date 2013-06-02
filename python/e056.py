from operator import add

def numbersum(n):
    z = [int(i) for i in str(n)]
    return reduce(add, z)

maxs = 0
for a in range(1,100):
    for b in range(1,100):
        maxs = max(maxs, numbersum(a**b))
        
print 'Ans: ', maxs
