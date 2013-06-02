from operator import mul
from operator import add

def isPal(n):
    z = [i for i in reversed(str(n))]
    zz = [i for i in str(n)]
    if z == zz:
        return True
    return False

def revs(n):
    z = [i for i in reversed(str(n))]
    return int(''.join(map(str, z)))

#print 234, revs(234)

ant = 0
for i in range(1, 10000):
    for s in range(1, 50):
        j = revs(i)
        r = i + j
        if isPal(r):
            break
        i = r
    if s == 49:
        ant = ant + 1
print 'Ans: ', ant
#n = 47
#z = [i for i in reversed(str(n))]
#zz = [int(i) for i in reversed(str(n))]

#print z, zz, map(int, z), int(''.join(map(str,z))), int(filter(str.isdigit, repr(z)))
#print reduce(lambda x, y: x + y, zz), reduce(mul, zz), reduce(add, zz)

#print 99**99


    
