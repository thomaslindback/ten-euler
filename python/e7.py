#
from math import sqrt

def is_prime2(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(sqrt(n))
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True
  
def is_prime(cand):
	limit = sqrt(cand) + 1
	d = 3
	while d <= limit:
		if  cand%d == 0:
			return False
		d += 2
	return True

print(is_prime(7))
print(is_prime(17))
print(is_prime(123))
print(is_prime(9))
print(is_prime(51329))
print(is_prime(74071))
print(is_prime(104729))

num = 1
numbers_of_prime = 1
while numbers_of_prime < 10001:
	num += 2
	if is_prime(num) == True:
		numbers_of_prime += 1
		print(num, numbers_of_prime)

print(num, numbers_of_prime)