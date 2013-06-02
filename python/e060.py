from math import sqrt
 
#primes = {}
#for i in range (2, 10000):
#    primes[i] = True
#def prime(n):
#    i = 2
#    while(i < sqrt(n) + 1):
#        if n % i == 0:
#            return False
#        i = i + 1
#    return True
#def test(one, two):
#    if prime(int(str(one) + str(two))) and prime(int(str(two) + str(one))):
#        return True
#    return False
#for i in range(2, 10000):
#    c = 2
#    j = i * 2
#    while(j < 10000):
#        primes[j] = False
#        c = c + 1
#        j = i * c
#for p1 in range(2, 10000):
#    if primes[p1]:
#        for p2 in range(p1, 10000):
#            if primes[p2] and test(p1, p2):
#                for p3 in range(p2, 10000):
#                    if primes[p3] and test(p1, p3) and test(p2, p3):
#                        for p4 in range(p3, 10000):
#                            if primes[p4] and test(p1, p4) and test(p2, p4) and test(p3, p4):
#                                for p5 in range (p4, 10000):
#                                    if primes[p5] and test(p1, p5) and test(p2, p5) and test(p3, p5) and test(p4, p5):
#                                        print str(p1) + " " + str(p2) + " " + str(p3) + " " + str(p4) + " " + str(p5)
#                                        print p1 + p2 + p3 + p4 + p5
#                                        raw_input()

def is_prime2(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True
primes = []
for i in range(3, 20000):
    if is_prime2(i):
        primes.append(i)
        
def ctest(one, two):
    if is_prime2(int(str(one) + str(two))) and is_prime2(int(str(two) + str(one))):
        return True
    return False


def search():
    global msum
    for i in range(0,plen):
        for j in range(i+1, plen):
            if ctest(primes[i], primes[j]):
                for k in range(j+1, plen):
                    if ctest(primes[i], primes[k]) and ctest(primes[j], primes[k]):
                        for ll in range(k+1, plen):
                            if ctest(primes[i], primes[ll]) and ctest(primes[j], primes[ll]) and ctest(primes[k], primes[ll]):
                                for m in range(ll+1, plen):
                                    if ctest(primes[i], primes[m]) and ctest(primes[j], primes[m]) and ctest(primes[k], primes[m]) and ctest(primes[ll], primes[m]):
                                        ss = primes[i]+ primes[j]+ primes[k]+ primes[ll]+ primes[m]                                        
                                        if ss < msum:
                                            msum = ss
                                            print msum, ': ', primes[i], primes[j], primes[k], primes[ll], primes[m]
    
msum = 200000
plen = len(primes)
#print plen
#print primes[plen-1]
search()
