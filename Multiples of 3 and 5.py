total = 0
for num in range(1000):
    if (num % 5 == 0) or (num % 3 == 0):
        total = total + num
print(total)
