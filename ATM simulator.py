balance = 5000

print("1.check balance")
print("2.withdraw money")
print("3.Exit")

choose = int(input("enter the number of the option you need :"))

if choose  == 1:

    print(balance)

elif choose == 2:

    pick = int(input("how much do you want to withdraw:"))

    if pick > balance:
        print("insufficient balance")

    else:
        balance = balance - pick
        print("balance = Rs.",balance)

elif choose == 3:
    
    print("goodbye")

else:
    print("invalid choice")


    
