search = input("enter your sentence : ")

target = input("enter the word :")

def search_word(search,target):

    word = search.split()
    count = 0

    for x in range(len(word)):

        if word[x] == target:

            count = count + 1

    return count

result = search_word(search,target)
print(target,"has appeared",result,"times")
        
