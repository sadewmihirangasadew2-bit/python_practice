numbers = [-5,12,-3,8,0,15,-2]

def sum_positive(numbers):

    total = 0

    for x in range(len(numbers)):

        if numbers[x] > 0:

            total = total + numbers[x]

    return total

result = sum_positive(numbers)
print("sum of positive numbers are :",result)
