#

sum1 = 0
sum2 = 0

for i in range(1,101):
	sum1 += i*i;
	sum2 += i
	
print(sum2*sum2 - sum1)

def p6():  
    n = 100  
    squareOfSum = ((n*(n+1))/2)**2  
    sumOfSquares = (n*(n+1)*(2*n+1))/6  
    print squareOfSum - sumOfSquares  

p6()