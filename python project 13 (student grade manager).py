number_of_students = int(input("how many students do you wish to enter :"))

for i in range(number_of_students):

    name = input("enter the students name :")
    marks = int(input("enter the marks :"))

    if marks < 0 or marks > 100:

        grade = "Error: Marks must be between 0 and 100" 

    elif marks >= 80 and marks <= 100:

        grade = "A"

    elif marks >= 70 and marks <= 79:

        grade = "B"

    elif marks >= 60 and marks <= 69:

        grade = "C"

    elif marks >= 50 and marks <= 59:

        grade = "D"
        
    else:
        grade = "FAIL"

    print("students name:",name)
    print("students marks :",marks)
    print("students grade :",grade)
    print("--------------------------------")
