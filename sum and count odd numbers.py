num = int(input("enter your number :"))

count = 0
total = 0

for x in range(1,num + 1):
    if x % 2 != 0:
        total = total + x
        count = count + 1

print("sum of odd numbers is :",total)
print("number of odd numbers is",count)
