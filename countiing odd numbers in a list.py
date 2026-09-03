numbers = [12,7,20,15,8,3,10]

count = 0

for x in range(len(numbers)):

    if numbers[x] % 2 != 0:
        count = count + 1

print("odd numbers :",count)
