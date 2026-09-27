search = input("enter your sentence :")

letter = int(input("enter your number :"))

def count_long(search,letter):

    words = search.split()
    count = 0

    for x in range(len(words)):

        if len(words[x])> letter:

            count = count + 1

    return count

result = count_long(search,letter)
print("result :",result)
