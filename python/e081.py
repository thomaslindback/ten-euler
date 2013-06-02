A = [[int(n) for n in s.split(',')] for s in open('matrix.txt').readlines()]

nrows = len(A)-1

for q in range(nrows, -1, -1):
    r = [r for r in range(nrows, q - 1, -1)]
    c = [c for c in reversed(r)]
    for x in range(0, len(r)):
        if r[x] == nrows and c[x] == nrows:
            print 'skipping 4, 4'
        else:
            #print '(', r[x], ',', c[x], ')'
            if r[x] == nrows:
                A[r[x]][c[x]] = A[r[x]][c[x]] + A[r[x]][c[x]+1]
            elif c[x] == nrows:
                A[r[x]][c[x]] = A[r[x]][c[x]] + A[r[x]+1][c[x]]
            else:
                A[r[x]][c[x]] = A[r[x]][c[x]] + min(A[r[x]+1][c[x]], A[r[x]][c[x]+1])
                
    #print '-'
print '++'

#for r in A:
#    print r
    
for q in range(nrows, -1, -1):
    c = [c for c in range(0, q)]
    r = [r for r in reversed(c)]
    for x in range(0, len(r)):
        #print '(', r[x], ',', c[x], ')'
        A[r[x]][c[x]] = A[r[x]][c[x]] + min(A[r[x]+1][c[x]], A[r[x]][c[x]+1])
    #print '-'

print A[0][0]
    
print 427337