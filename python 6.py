box = input("eenter your sentence :")

def count_lower(box):

    count = 0

    for x in range(len(box)):

        if box[x].islower():

            count = count + 1

    return count

result = count_lower(box)
print("number of lowercase letters are :",result)
