
def triag(n):
    return n * (n + 1) / 2
def square(n):
    return n * n
def penta(n):
    return n * (3 * n - 1) / 2
def hexa(n):
    return n * (2 * n - 1)
def hepta(n):
    return n * (5 * n - 3) / 2
def octa(n):
    return n * (3 * n - 2)

tris = [(3, triag(x)) for x in range(0, 200) if triag(x) >= 1000 and triag(x) < 10000]
sqrs = [(4, square(x)) for x in range(0, 200) if square(x) >= 1000 and square(x) < 10000]
pents = [(5, penta(x)) for x in range(0, 200) if penta(x) >= 1000 and penta(x) < 10000]
hexs = [(6, hexa(x)) for x in range(0, 200) if hexa(x) >= 1000 and hexa(x) < 10000]
hepts = [(7, hepta(x)) for x in range(0, 200) if hepta(x) >= 1000 and hepta(x) < 10000]
octs = [(8, octa(x)) for x in range(0, 200) if octa(x) >= 1000 and octa(x) < 10000]
print len(tris), tris
print len(sqrs), sqrs
print len(pents), pents
print len(hexs), hexs
print len(hepts), hepts
print len(octs), octs

def fn(n):
    return (3, n * (n + 1) / 2), (4, n * n), (5, n * (3 * n - 1) / 2), (6, n * (2 * n - 1)), (7, n * (5 * n - 3) / 2), (8, n * (3 * n - 2))

p = []
n = 1
while n < 141:
    for t, data in fn(n):
        if 1000 <= data <= 9999 and data % 100 > 9:
            p.append((t, data)) 
    n += 1
print len(p), p
print 96 + 68 + 56 + 48 + 43 + 40

ds = {}         # build a dictionary of tuples
for t1, d1 in p:
    for t2, d2 in p:
        if t1 != t2 and d1 % 100 == d2 // 100:
            ds[t1, d1] = ds.get((t1, d1), []) + [(t2, d2)]
print ds
print ds[(3, 5886)]

def nextt(types, data):
    if len(types)==6 and data[0]//100 == data[-1]%100:
        print data, sum(data)
    else:
        for t, n in ds.get((types[-1], data[-1]), []):
            if t not in types:
                nextt(types+[t], data+[n])
for t, data in ds: nextt([t],[data])