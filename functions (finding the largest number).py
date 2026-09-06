numbers = [12,45,7,89,23,56]

def find_largest(numbers):

    largest = 0

    for x in range(len(numbers)):

        if numbers[x] > largest:

            largest = numbers[x]

    return largest

result = find_largest(numbers)
print("largest number is :",result)

    
        
