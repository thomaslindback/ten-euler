from math import sqrt

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

diagPrimes = []
startValue = 2
for i in range(2, 30000, 2):
    v = range(startValue, 4 * i + startValue)  
    diagElems = i + (i + 1)  
    corners = v[i - 1::i]
    for p in corners:
        if is_prime2(p):
            diagPrimes.append(p)

    if 1.0*len(diagPrimes)/diagElems < 0.1:
        print 'sidelen:', (i+1), 1.0*len(diagPrimes)/diagElems
        break
    #print i, 4 * i, diagElems, corners
    startValue = v[len(v) - 1] + 1
    
