search = input("enter your sentence :")

def longest_word_length(search):

    word = search.split()
    longest = word[0]

    for x in range(len(word)):

        if len(word[x])> len(longest):

            longest = word[x]

    return len(longest)

result = longest_word_length(search)
print("the longest word length is :",result)
