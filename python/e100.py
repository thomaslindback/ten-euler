#
#  P(BB) = (15/21)(14/20) = 1/2

def xs(x):
    return x * (x - 1)

no_balls = 10 ** 12
#no_balls = 21
goal = no_balls * (no_balls - 1) / 2
print 'goal ', goal

lower = 0
upper = 10 ** 15
#upper = 100

for i in range(0, 60):
    testp = lower + (upper - lower) / 2
    tmp = xs(testp)
    print lower, upper, testp, tmp
    if tmp < goal:
        lower = testp;
    elif tmp > goal:
        upper = testp
    else:
        print 'done', testp
        break
    

print 707106781187.0 * (707106781187 - 1) / no_balls / (no_balls - 1)
print 707106781186.0 * (707106781186 - 1) / no_balls / (no_balls - 1)
print 756872327473.0 * (756872327473 - 1) / no_balls / (no_balls - 1)


b = 85
n = 120
while n < 10**12:
    b,n = 3*b + 2*n - 2, 4*b + 3*n - 3
print "Answer to PE100 = ",b