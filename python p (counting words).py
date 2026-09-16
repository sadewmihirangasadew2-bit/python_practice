search = input("enter your sentence :")

def count_words(search):

    count = 0
    word = search.split()

    for x in range(len(word)):

        count = count + 1

    return count

result = count_words(search)
print("number of words :",result)
