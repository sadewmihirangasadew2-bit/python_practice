numbers = []

for x in range(5):

    number = int(input("enter a number :"))
    numbers.append(number)

print(numbers)

total = sum(numbers)
print("total :",total)

average = sum(numbers)/ len(numbers)
print("average :",average)

largest = max(numbers)
print("largest number :",largest)

    

    
