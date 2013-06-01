# euler9
from operator import mul

t = [8, 15, 17]
# k*t = pythagoran triple too
t1 = [25*i for i in t]

print(t1)
print('a**2+b**2: ', t1[0]**2 + t1[1]**2)
print('c**2: ', t1[0]**2 + t1[1]**2)
print('sum: ', t1[0] + t1[1] + t1[2])
print('a*b*c: ', t1[0] * t1[1] * t1[2])
print('a*b*c: ', reduce(mul, t1))

