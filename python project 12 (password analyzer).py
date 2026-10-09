text = input("enter your password :")

def analyze(text):

    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_count = 0

    for x in range(len(text)):

        if text[x].isupper():

            uppercase_count = uppercase_count + 1

        if text[x].islower():

            lowercase_count = lowercase_count + 1

        if text[x].isdigit():

            digit_count = digit_count + 1

        if not text[x].isalpha()and not text[x].isdigit() and not text[x] == " ":

            special_count = special_count + 1

    return uppercase_count,lowercase_count,digit_count,special_count

uppercase_count,lowercase_count,digit_count,special_count = analyze(text)
print("uppercase letters :",uppercase_count)
print("lowercase letters :",lowercase_count)
print("digits present :",digit_count)
print("special characters",special_count)
print("total",len(text))

#password strength checker

if len(text) < 8 :
    
    print("your password is weak")

elif uppercase_count > 0 and digit_count > 0 and special_count > 0:
    
     print("your password strength is strong")

else:
     print("your password is medium")


