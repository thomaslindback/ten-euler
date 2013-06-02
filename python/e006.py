# Project Euler 6

def e6(n):  
    squareOfSum = ((n*(n+1))/2)**2  
    sumOfSquares = (n*(n+1)*(2*n+1))/6  
    return squareOfSum - sumOfSquares  

print e6(100)

r = range(1, 101)
print sum([i for i in r])**2 - sum([i*i for i in r])