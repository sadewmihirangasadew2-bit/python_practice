search = input("enter your sentence :")

target = input("enter your character :")

def count_character(search,target):

    count = 0

    for x in range(len(search)):

        if search[x].lower()== target.lower():

            count = count + 1

    return count

result = count_character(search,target)
print(target,"has appeared",result,"times")
