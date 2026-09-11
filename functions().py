text = "python 123 is fun"

def analyze(text):

        vowel_count = 0
        consonent_count = 0
        digit_count = 0
        space_count = 0

        for x in range(len(text)):

            if text[x] in "aeiou":

                vowel_count = vowel_count + 1

            if text[x].isalpha()and text[x] not in "aeiou":

                consonent_count = consonent_count + 1

            if text[x].isdigit():

                digit_count = digit_count + 1

            if text[x]== " ":

                space_count = space_count + 1

        return  vowel_count,consonent_count,digit_count,space_count

result = vowel_count,consonent_count,digit_count,space_count = analyze(text)
print("number of vowels are :",vowel_count)
print("number of consonents are :",consonent_count)
print("number of digits are :",digit_count)
print("number of spaces are :",space_count)


                

            
