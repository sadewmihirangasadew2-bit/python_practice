bag = input("enter your sentence :")

def count_upper(bag):
    
    count = 0

    for x in range(len(bag)):

        if bag[x].isupper():

            count = count + 1

    return count

result = count_upper(bag)
print("number of uppercase letters are :",result)
