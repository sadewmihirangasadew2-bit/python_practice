search = input("enter your sentence :")

starbucks = int(input("enter your number :"))

def count_length(search,starbucks):

    word = search.split()
    count = 0

    for x in range(len(word)):

        if len(word[x])>= starbucks:

            count = count + 1

    return count

result = count_length(search,starbucks)
print("the result is :",result)
