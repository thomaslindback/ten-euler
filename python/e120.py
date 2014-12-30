
# 2an = r mod a**2 => 2an = ma**2 is minimized for any m
# max for n = (a-1)/2

print sum([2*a*((a-1)/2) for a in range(3, 1001)])
