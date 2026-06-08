def calc():

    ca = int(input("enter num 1:"))
    ba = int(input("enter num 2:"))
    sa = (input("choose +,-,*,/"))

    if sa == "+":
        print("result :",ca + ba)

    elif sa == "-":
        print("result:",ca - ba)

    elif sa == "*":
        print("result",ca * ba)

    elif sa == "/":
        print("result",ca / ba)

calc()
        
