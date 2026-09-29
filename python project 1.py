ben = input("enter your sentnece : ")

def count_consonants(ben):

    word = ben.split()
    count = 0

    for x in range(len(word)):

        for y in range(len(word[x])):

            if word[x][y].isalpha() and word[x][y]not in "aeiou":

                count = count + 1

    return count

result = count_consonants(ben)
print("number of consonants are :",result)
