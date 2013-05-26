# Project Euler 4

import itertools

def isPalindrome(n):
	return str(n) == str(n)[::-1]

print max([ a*b for (a,b) in itertools.permutations(range(100, 1000), 2) if isPalindrome(a*b)])

