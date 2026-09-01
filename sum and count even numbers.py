num = int(input("enter your number :"))

count = 0
total = 0

for x in range(1,num + 1):
    total = total + x
    if x % 2 == 0 :
        count = count + 1

print("sum is :",total)
print("even numbers :",count)
