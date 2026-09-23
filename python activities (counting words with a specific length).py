search = input("enter your sentence :")

target = int(input("enter your length :"))

def count_length(search,target):

    word = search.split()
    count = 0

    for x in range(len(word)):

        if len(word[x])== target:

            count = count + 1

    return count

result = count_length(search,target)
print("words with length :",result)
