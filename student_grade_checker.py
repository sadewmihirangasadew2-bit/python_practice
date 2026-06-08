def analyze_mark(mark):

    if mark < 50:
        return "fail"
    
    elif 50 <= mark <= 74:
        return "pass"

    else:
        return "distinction"

mark = int(input("enter your marks:"))

answer = analyze_mark(mark)

print("your grade is :",answer)

if answer == "distinction":
    print("excellent work")

elif answer == "pass":
    print("good job")

else:
    print("keep practicing")

print("do you have any more marks??",yes/no)
