numbers = [-5,12,-3,8,0,15,-2]

def count_positive(numbers):

    count = 0

    for x in range(len(numbers)):

        if numbers[x] > 0:

            count = count + 1

    return count

result = count_positive(numbers)
print("number of positive numbers are :",result)
