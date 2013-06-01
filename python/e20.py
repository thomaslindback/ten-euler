# euler 20

from operator import mul

result = sum(map(int, list(str(reduce(mul, range(1,101))))))
print('result: ', result)