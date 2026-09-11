text = "python is a very useful programming language"

def count_words(text):

    count = 0
    word = text.split()

    for x in range(len(word)):

        count = count + 1

    return count

result = count_words(text)
print("number of words are :",result)
