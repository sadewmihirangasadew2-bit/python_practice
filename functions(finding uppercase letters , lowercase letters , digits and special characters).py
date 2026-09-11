text = "Hello WORLD 123 python !"

def analyze(text):
    
    upper_count = 0
    lower_count = 0
    digit_count = 0
    special_count = 0

    for x in range(len(text)):

        if text[x].isupper():

            upper_count = upper_count + 1

        if text[x].islower():

            lower_count = lower_count + 1

        if text[x].isdigit():

            digit_count = digit_count + 1

        if not text[x].isalpha() and not text[x].isdigit() and text[x]!= " ":

            special_count = special_count + 1

    return upper_count , lower_count , digit_count , special_count

result = upper_count , lower_count , digit_count , special_count = analyze(text)
print("number of uppercase letters are :",upper_count)
print("number of lowercase letters are :",lower_count)
print("number of digits are :",digit_count)
print("numbers of special characters are :",special_count)

        

