
print('Euler 80')

from math import sqrt

def init(n):
    return (5*n, 5)

def step(p):
    (a,b) = p
    if a >= b:
        return (a-b, b+10)
    else:
        s = str(b)
        s = s[:len(s)-1] + "05"
        return (a*100, int(s))

def calc(n, max_len):
    p = init(n)
    while len(str(p[1])) < max_len+4:
        #print(p)
        p = step(p)
        if p[0] == 0:
            st = str(p[1])
            return st[0:len(st)-1]
                             
    return str(p[1])[0:max_len]

def sum_letters(rs):
    return sum(map(int, rs))

all_sum = 0
for i in range(1, 100):
    res = calc(i, 100)
    if len(res) == 100:
        all_sum += sum_letters(res)
        
print('Result: ', all_sum)
      
