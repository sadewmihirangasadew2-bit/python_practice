numbers = [5,12,7,20,9,14,3]

def sum_even(numbers):

    total = 0

    for x in range(len(numbers)):

        if numbers[x] % 2 == 0:

            total = total + numbers[x]

    return total

result = sum_even(numbers)
print("sum of even numbers are",result)
