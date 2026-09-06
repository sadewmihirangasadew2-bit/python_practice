numbers = [15,8,23,42,17,30,11]

largest = numbers[0]

for x in range(len(numbers)):
    
    if numbers[x] > largest and numbers[x] % 2 == 0:

        largest = numbers[x]

print("largest even number is",largest)
