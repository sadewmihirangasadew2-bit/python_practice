search = input("enter your sentnce :")

target = input("enter your letter :")

def count_starting(search,target):

    word = search.split()
    count = 0

    for x in range(len(word)):

        if word[x][0].lower()== target.lower():

            count = count + 1

    return count

result = count_starting(search,target)
print("words starting with",target,result)
