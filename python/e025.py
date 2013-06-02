# euler25

from math import log10, ceil, sqrt
phi = (1+sqrt(5))/2 
digits = 1000
 
f_term = ceil((digits-1 + log10(5)/2) / log10(phi))
print "Answer to PE25 = ", int(f_term)

#LOG (Phi^1000/sqr5)
#1000*LOG(Phi) - (LOG sqr5) = 1000*LOG(Phi) - (LOG 5)/2 = number digits in F(1000) -1
#1+int(a) = F(1000) 
# 
# 
def get_fib_with_digits(numdigits):
	return ceil((numdigits-1 + log10(5)/2)/log10(phi))
print(int(get_fib_with_digits(1000)))
	
def number_of_digits_in_fib(num):
	return 1+int(num*log10(phi) - log10(5)/2)
	
print(number_of_digits_in_fib(1000))
print(number_of_digits_in_fib(2000))
print(number_of_digits_in_fib(3000))
print(number_of_digits_in_fib(4000))
print(number_of_digits_in_fib(5000))
print(number_of_digits_in_fib(4700))
print(number_of_digits_in_fib(4800))
print(number_of_digits_in_fib(4750))
print(number_of_digits_in_fib(4760))
print(number_of_digits_in_fib(4770))
print(number_of_digits_in_fib(4780))
print(number_of_digits_in_fib(4790))
print(number_of_digits_in_fib(4781))
print(number_of_digits_in_fib(4782))
print(number_of_digits_in_fib(4783))
print(number_of_digits_in_fib(4784))
