# euler15

# 40!/20!20!
from operator import mul

result = reduce(mul, range(1,41))/reduce(mul, range(1,21))/reduce(mul, range(1,21))
print(result)