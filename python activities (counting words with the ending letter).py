search = input("enter your sentence :")

target = input("enter your word :")

def count_ending(search,target):

    word = search.split()
    count = 0

    for x in range(len(word)):

        if word[x][-1].lower()== target.lower():

            count = count + 1

    return count

result = count_ending(search,target)
print("words starting with",target,result)
