# euler 33
from operator import mul

# numerator/denominator
# yx
# --
# xz

# x = 1 -> 9
# y = 1 -> 9
# z = 0 -> 9

yy = []
zz = []
for x in range(1,10):
	for y in range(1,10):
		for z in range(1,10):
			if y != x and x != z:
				nume = 10*y+x
				deno = float(x)*10+z
				if nume/deno == float(y)/z:
					print(nume,deno, y, z)
					yy.append(y)
					zz.append(z)


print(reduce(mul,yy))
print(reduce(mul,zz))