target = input("enter your word :")

def count_vowel(target):

    count = 0

    for x in range(len(target)):

        if target[x] in "aeiou":

            count = count + 1

    return count

result = count_vowel(target)
print("number of vowels are",result)
