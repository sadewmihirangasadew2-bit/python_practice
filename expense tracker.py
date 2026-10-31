x = 0
i = int(input("How many expenses??:"))
total = 0

while x < i:
    
    num = input("Enter your expense:")

    amo = float(input("Enter your expense amount:"))

    print("Expense recorded!!")
    print("Expense:",num)
    print("Amount:",amo)
    print("**------------------------------------------**")

    x += 1
    total += amo
    
print("final total is:",total)
