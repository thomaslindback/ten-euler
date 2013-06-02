

# [1;2,2,2,2,2,2,...]

def calculate(a):
    h2 = 0
    h1 = 1
    k2 = 1
    k1 = 0
    for i in range(0, len(a)):
        h0 = a[i] * h1 + h2
        k0 = a[i] * k1 + k2
        
        h2 = h1
        h1 = h0
        
        k2 = k1
        k1 = k0
    return h0, k0
         

print calculate([1, 2])
print calculate([1, 2, 2])
print calculate([1, 2, 2, 2])
print calculate([1, 2, 2, 2, 2])
print calculate([1, 2, 2, 2, 2, 2])
print calculate([1, 2, 2, 2, 2, 2, 2])
print calculate([1, 2, 2, 2, 2, 2, 2, 2])
print calculate([1, 2, 2, 2, 2, 2, 2, 2, 2])

o = 0
for y in range(1, 1001):
    num, den = calculate([1] + [2] * y)
    if len(str(num)) > len(str(den)):
        o = o + 1
print o