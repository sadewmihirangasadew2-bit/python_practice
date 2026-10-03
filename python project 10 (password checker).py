send = input("enter your password :")

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


    if uppercase_count > 0 and lowercase_count > 0 and digit_count > 0 and special_count >0:

        return "password meets all requirements"
    else:
        return "password does not meet all requirements"

result = analyze(send)
print(result)


    
