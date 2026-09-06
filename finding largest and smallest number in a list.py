numbers = [12,7,25,8,30,15,42,9]

largest = numbers[0]

smallest = numbers[0]

for x in range(len(numbers)):

    if numbers[x] > largest:
        
        largest = numbers[x]
        
    if numbers[x] < smallest:

        smallest = numbers[x]
        

 print("largest numbers is",largest)  
 print("smallest numbers is",smallest)

