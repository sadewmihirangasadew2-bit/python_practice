def largest(a,b):
    if a > b:
        return a
    else:
        return b

a = int(input("enter num 1:"))
b = int(input("enter num 2:"))

answer = largest(a,b)

print ("the largest number is :",answer)
