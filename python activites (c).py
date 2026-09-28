stank = input("enter your sentence :")

def count_consonants(stank):

    word = stank.split()
    count = 0

    for x in range(len(word)):

        for y in range(len(word[x])):

            if word[x][y].isalpha() and word[x][y]not in "aeiou"  :

                count = count + 1

    return count

result = count_consonants(stank)
print("number of consonants :",result)
