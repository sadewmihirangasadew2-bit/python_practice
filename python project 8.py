wend = input("enter your sentence :")

def analyze_text(wend):

    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0

    for x in range(len(wend)):

        if wend[x].isupper():

            uppercase_count = uppercase_count + 1

        if wend[x].islower():

            lowercase_count = lowercase_count + 1

        if wend[x].isdigit():

            digit_count = digit_count + 1

    return uppercase_count,lowercase_count,digit_count

result = uppercase_count,lowercase_count,digit_count = analyze_text(wend)
print("number of uppercase letters :",uppercase_count)
print("number of lowercase letters :",lowercase_count)
print("number of digits :",digit_count)
