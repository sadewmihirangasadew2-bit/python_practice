search = input("enter your sentence :")

def analyze(search):

    upper_count = 0
    lower_count = 0
    digit_count = 0
    special_count = 0

    for x in range(len(search)):

        if search[x].isupper():

            upper_count = upper_count + 1

        if search[x].islower():

            lower_count = lower_count + 1

        if search[x].isdigit():

            digit_count = digit_count + 1

        if not search[x].isalpha() and not search[x].isdigit() and search[x] != " ":

            special_count = special_count + 1

    return upper_count,lower_count,digit_count,special_count

result = upper_count,lower_count,digit_count,special_count = analyze(search)
print("uppercase :",upper_count)
print("lowercase :",lower_count)
print("digits :",digit_count)
print("special characters :",special_count)
