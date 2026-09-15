search = input("enter your sentence :")

target = input("enter your word :")

def search_word(search,target):

    word = search.split()
    count = 0

    for x in range(len(word)):

        if word[x].lower() == target.lower() :

            count = count + 1

    return count

result = search_word(search,target)
print(target,"has appeared",result,"times")
