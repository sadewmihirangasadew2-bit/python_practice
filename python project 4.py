upchuck = input("enter your sentence :")

def count_digits(upchuck):

    count = 0

    for x in range(len(upchuck)):

        if upchuck[x].isdigit():

            count = count + 1

    return count

result = count_digits(upchuck)
print("number of digits are :",result)
