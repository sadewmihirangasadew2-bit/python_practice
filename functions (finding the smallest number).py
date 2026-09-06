numbers = [34,12,56,7,89,23]

def find_smallest(numbers):

    smallest = numbers[0]

    for x in range(len(numbers)):

        if numbers[x] < smallest:

            smallest = numbers[x]

    return smallest

result = find_smallest(numbers)
print("smallest number is :",result)
