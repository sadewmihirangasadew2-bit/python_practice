search = input("enter your sentence :")

ralphs = int(input("enter your number :"))

def count_short(search,ralphs):

    word = search.split()
    count = 0

    for x in range(len(word)):

        if len(word[x]) < ralphs:

            count = count + 1

    return count

result = count_short(search,ralphs)
print("the result is  :",result)
