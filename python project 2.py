gwen = input("enter your sentence : ")

def count_vowels_consonants(gwen):

    word = gwen.split()
    vowel_count = 0
    consonant_count = 0

    for x in range(len(word)):

        for y in range(len(word[x])):

            if word[x][y].lower() in "aeiou":

                vowel_count = vowel_count + 1

            if word[x][y].isalpha() and word[x][y].lower()not in "aeiou":

                consonant_count = consonant_count + 1

    return vowel_count,consonant_count

result = vowel_count,consonant_count = count_vowels_consonants(gwen)
print("number of vowels are :",vowel_count)
print("number of consonants are :",consonant_count)

    
