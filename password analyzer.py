password = input("enter your password :")

def analyze(password):

    up_count = 0
    lo_count = 0
    digit_count = 0
    sp_count = 0

    for x in range(len(password)):

        if password[x].isupper():

            up_count += 1

        if password[x].islower():

            lo_count += 1

        if password[x].isdigit():

            digit_count += 1

        if not password[x].isalpha() and not password[x].isdigit()and password[x] != " ":

            sp_count += 1

    total_length = len(password)

    return up_count,lo_count,digit_count,sp_count,total_length

result = up_count,lo_count,digit_count,sp_count,total_length = analyze(password)
print("uppercase :",up_count)
print("lo_count :",lo_count)
print("digits :",digit_count)
print("special characters :",sp_count)
print("total:",total_length)



