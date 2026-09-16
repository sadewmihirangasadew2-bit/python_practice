search = input("enter a sentence :")

def vowels_count(search):

    count = 0

    for x in range(len(search)):

        if search[x] in "aeiou":

            count = count + 1

    return count

result = vowels_count(search)
print("number of vowels are :",result)
