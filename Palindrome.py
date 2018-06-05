def isPalindrome(string):
    length= len(string)
    for index in range(length//2 + 2):
        if string[index] != string[-1-index]:
            return False
    return True
largest = [0,0,0]
for num1 in range(100,1000):
    for num2 in range(100,1000):
        prod = num1*num2
        if prod > largest[0] and isPalindrome(str(prod))==True:
            largest = [prod, num1, num2]
print(largest)
            
        
        
