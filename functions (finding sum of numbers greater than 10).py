numbers = [5,18,7,25,12,3,30]

def sum_greater_than_10(numbers):

    total = 0

    for x in range(len(numbers)):

        if numbers[x] > 10:

            total = total + numbers[x]

    return total

result = sum_greater_than_10(numbers)
print("sum is :",result)
