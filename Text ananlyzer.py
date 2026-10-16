text = input("enter your text that needs to be analyzed :")

def analyze_text(text):
    
    words = text.split()
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    uppercase_count = 0

    for x in range(len(words)):

        for y in range(len(words[x])):


            if words[x][y].lower()in "aeiou":

                vowel_count += 1

            if words[x][y].isalpha()and words[x][y].lower()not in "aeiou" :

                consonant_count += 1

            if words[x][y].isdigit():

                digit_count += 1

            if words[x][y].isupper():

                uppercase_count += 1

    total = len(words)

    return vowel_count,consonant_count,digit_count,uppercase_count,total

vowel_count, consonant_count, digit_count, uppercase_count, total = analyze_text(text)
print("vowels :",vowel_count)
print("consonants :",consonant_count)
print("digit :",digit_count)
print("uppercase :",uppercase_count)
print("total:",total)
