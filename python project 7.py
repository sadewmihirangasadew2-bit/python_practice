ultra = input("enter your sentence :")

def count_all(ultra):

    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0

    for x in range(len(ultra)):

        if ultra[x].isupper():

            uppercase_count = uppercase_count + 1

        if ultra[x].islower():

            lowercase_count = lowercase_count + 1

        if ultra[x].isdigit():

            digit_count = digit_count + 1
            
    return uppercase_count,lowercase_count,digit_count

result = uppercase_count,lowercase_count,digit_count = count_all(ultra)
print("number of uppercase letters :",uppercase_count)
print("number of lowercase letters:",lowercase_count)
print("number of digits:",digit_count)

        
