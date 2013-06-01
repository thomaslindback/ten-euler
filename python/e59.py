
f = open('cipher1.txt', 'r')
s = f.read()
print s
A = [int(n) for n in s.split(',')]

print A
print A[0::3]

print ord('g')
print chr(97)
print chr(122)
print '-'
print 46^103
print 46^111
print 46^100
print '-'

dic = {}
for a in A:
    if a in dic:
        dic[a] = dic[a] + 1
    else: 
        dic[a] = 1

#pprint(dic)

dsum = 0
for i in range(2, len(A), 3):
        r1 = A[i - 2] ^ 103
        r2 = A[i - 1] ^ 111
        r3 = A[i - 0] ^ 100       
        print chr(r1), chr(r2), chr(r3) 
        dsum = dsum + r1
        dsum = dsum + r2
        dsum = dsum + r3
        
r1 = A[len(A)-1] ^ 103
print chr(r1)
print dsum + r1
