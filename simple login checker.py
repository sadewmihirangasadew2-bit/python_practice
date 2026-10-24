correct_user = "admin"
correct_pas = "python123"

user = input("enter your username :")
pas = input("enter your password :")

if user == correct_user and pas == correct_pas:

    print("access granted")
    print("username and password are correct!")

else:
    print("invalid password or username")
