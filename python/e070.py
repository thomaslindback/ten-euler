from math import sqrt
from itertools import combinations

print 'start'

def is_perm(a, b): return sorted(str(a)) == sorted(str(b))

def comp(n):
    if n % 2 == 0:
        return 2
    for i in range(3, 1 + n, 2):
        if n % i == 0:
            return i
    return -1


def calc_comps(num):
    dic = {}
    while True:
        c = comp(num)
        if c != -1:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
            num = num / c
        else:
            break
    return dic
        

def eulers(n):
    ks = [k for k in calc_comps(n).iterkeys()]
    tmp = 1
    for p in ks:
        tmp = tmp * (1 - (1.0 / p))
    return n * tmp

def eulers2(n, ks):
    tmp = 1
    for p in ks:
        tmp = tmp * (1 - (1.0 / p))
    return n * tmp

#print(is_perm(int(eulers(87109)), 87109))

# if p is prime totient = p-1
# if n = p1 * p2 totient = (p1-1)*(p2 - 1)

def totient2p(p1, p2):
    return (p1-1)*(p2-1)
f = open('primes5000.txt', 'r')
ps = []
for s in f:
    ps.append(int(s))
print ps
f.close()
print f

min_tot = 10**7
for c in combinations(ps, 2):
    num = c[0]*c[1]
    if num <= 10**7:
        titi = totient2p(c[0], c[1])
        if is_perm(num, titi):
            if 1.0*num/titi < min_tot:
                min_tot = 1.0*num/titi
                print num, titi, 1.0*num/titi
    
print 'end'