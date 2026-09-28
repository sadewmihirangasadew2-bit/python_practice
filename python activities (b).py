mark = input("enter your sentence :")

def count_vowels(mark):

    word = mark.split()
    count = 0

    for x in range(len(word)):

        for y in range(len(word[x])):

            if word[x][y].lower()in "aeiou":

                count = count + 1

    return count

result = count_vowels(mark)
print("the number of vowels are :",result)

