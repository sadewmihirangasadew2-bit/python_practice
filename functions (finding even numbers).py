numbers = [12,7,20,15,8,3,10]

def count_even(numbers):

    count = 0

    for x in range(len(numbers)):

        if numbers[x] % 2 == 0:

            count = count + 1

    return count

result = count_even(numbers)
print("number of even numbers are :",result)
