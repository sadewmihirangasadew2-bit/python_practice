search = input("enter your sentence :")

target = input ("enter your word :")

def count_characters(search,target):

    count = 0

    for x in range(len(search)):

        if search[x].lower()== target.lower():

            count = count + 1

    return count

result = count_characters(search,target)
print(target,"has appeared",result,"times")
