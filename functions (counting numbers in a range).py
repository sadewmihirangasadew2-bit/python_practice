numbers =[5,12,18,25,7,30,15,3]

def count_range(numbers):

    count = 0

    for x in range(len(numbers)):

        if 10 <= numbers[x] <= 20:

            count = count + 1

    return count

result = count_range(numbers)
print("numbers between 10 and 20 are :",result)
