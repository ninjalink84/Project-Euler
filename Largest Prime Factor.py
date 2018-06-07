import math
number = 600851475143
def isPrime(num1):
    for div in range(2,int(math.sqrt(num1))+1):
        if num1 % div == 0:
            return False
    return True
for x in range(1,number):
    if isPrime(x) == True and number % x == 0:
        topdiv = x
print(topdiv)

