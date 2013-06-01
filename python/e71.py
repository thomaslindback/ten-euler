from utils import gcd

N = 3/7.
L = 1000000
mina = N
for b in range(L, L-7, -1):
    a = N - int(b*N) * 1.0/b
    if mina > a != 0: mina, minD = a,b
 
print "Answer to PE71 =", int(minD*N), "/", minD

print gcd(56*7, 78*7)
goal = 3.0/7
print goal

m_num = 4
m_den = 1

cmin = 200

for num in range(421262, 430000):
    for den in range(989586, 1000000):
        res = 1.0*num/den
        if res <  goal:
            #print num, den, 1.0*num/den
            if goal - res < cmin:
                m_num = num
                m_den = den 
                cmin = goal - res
            break
print 'result:', m_num, m_den, 1.0*m_num/m_den      
print 'end'

