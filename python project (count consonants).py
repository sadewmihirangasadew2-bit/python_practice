search = input("enter your sentence :")

def count_consonants(search):

    count = 0

    for x in range(len(search)):

        if search[x].isalpha() and search[x] not in "aeiou":

            count = count + 1

    return count

result = count_consonants(search)
print("number of consonanats are :",result)
