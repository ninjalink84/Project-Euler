def primeFactor(num):
    #this function will take a number and output its prime factorization as a list
    factor = []
    #when a prime divides the number, it will be factored out of the number then added to the list
    #2,3,and 5 are best handled as special cases
    while num%2 == 0:
        factor = factor + [2]
        num = num//2
    while num%3 ==0:
        factor = factor + [3]
        num = num//3
    while num%5 ==0:
        factor = factor + [5]
        num = num//5
    #all primes are 1 or 5 modulo 6, so it is much more efficient to only check these numbers
    index = 1
    while index <= (num/6) + 1:
        while num % ((index * 6) + 1)== 0:
            factor = factor + [(index * 6) + 1]
            num = num//((index * 6) + 1)
        while num % ((index * 6) + 5)== 0:
            factor = factor + [(index * 6) + 5]
            num = num//((index * 6) + 5)
        index = index + 1
    return factor
userNum = int(input('What number would you like factored?\n'))
print(primeFactor(userNum))
