numbers = [10,20,30,40,50]

smallest = numbers[0]

for x in range(len(numbers)):

    if numbers[x] < smallest:
        smallest = numbers[x]

print("smallest is :",smallest)
    
