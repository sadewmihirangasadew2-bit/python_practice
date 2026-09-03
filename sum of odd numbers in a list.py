numbers = [12,7,20,15,8,3,10]

total = 0

for x in range(len(numbers)):

    if numbers[x] % 2 != 0:
        total = total + numbers[x]

print("sum of odd numbers :",total)

