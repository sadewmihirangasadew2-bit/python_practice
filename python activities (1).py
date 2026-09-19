search = input("enter your sentence :")

target = input("enter the word to search :")

def specific_count(search,target):

    word = search.split()
    count = 0

    for x in range(len(word)):

        if word[x] == target:

            count = count + 1

    return count

result = specific_count(search,target)
print(target,"has appeared ",result,"times")
