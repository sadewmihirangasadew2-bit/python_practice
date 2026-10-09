send = input("enter your sentence :")

def analyze_text(send):

    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0

    for x in range(len(send)):

        if send[x].isupper():

            uppercase_count = uppercase_count + 1

        if send[x].islower():

            lowercase_count = lowercase_count + 1

        if send[x].isdigit():

            digit_count = digit_count +  1

    return uppercase_count,lowercase_count,digit_count

result = uppercase_count,lowercase_count,digit_count = analyze_text(send)
print("number of uppercase letters are :",uppercase_count)
print("number of lowercase letters are :",lowercase_count)
print("number of digits are :",digit_count)

            

    
