def is_positive(num):

    if num > 0:
        return "positive"
    else:
        return "not positive"

num = int(input("enter your number:"))

answer = is_positive(num)

print("your number is :",answer)
