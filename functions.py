def check_number(number):

    if number > 0:
        return "positive"

    elif number < 0: 
        return "negative"

    else:
        return "zero"

result = check_number(0)
print(result)
    
