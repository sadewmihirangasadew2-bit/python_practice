send = input("enter your sentence :")

def analyze(send):

    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_count = 0

    for x in range(len(send)):

        if send[x].isupper():

            uppercase_count = uppercase_count + 1

        if send[x].islower():

            lowercase_count = lowercase_count + 1

        if send[x].isdigit():

            digit_count = digit_count + 1

        if not send[x].isalpha() and not send[x].isdigit() and send[x] !=" ":

            special_count = special_count + 1

    return uppercase_count,lowercase_count,digit_count,special_count

result = uppercase_count,lowercase_count,digit_count,special_count = analyze(send)
print("uppercase :",uppercase_count)
print("lowercase :",lowercase_count)
print("digit :",digit_count)
print("special characters :",special_count)
