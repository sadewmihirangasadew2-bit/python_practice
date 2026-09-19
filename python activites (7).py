search = input("enter your sentence : ")

def count_words(search):

    words = search.split()
    count = 0

    for x in range(len(words)):

        count = count + 1

    return count

result = count_words(search)
print("number of words are :",result)
