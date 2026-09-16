search = input("enter a sentence :")

def count_digits(search):

    count = 0

    for x in range(len(search)):

        if search[x].isdigit():

            count = count + 1

    return count

result = count_digits(search)
print("number of digits are :",result)
