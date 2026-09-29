grand = input("enter your sentence : ")

def count_digits(grand):

    count = 0

    for x in range(len(grand)):
        
            if grand[x].isdigit():

                count = count + 1

    return count

result = count_digits(grand)
print("number of digits are :",result)
