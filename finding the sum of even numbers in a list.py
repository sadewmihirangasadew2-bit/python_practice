numbers = [5,12,7,20,9,14,3]

total = 0

for x in range(len(numbers)):

    if numbers[x] % 2 == 0:
        
        total =total + numbers[x]

print("sum of even numbers are",total)

    
