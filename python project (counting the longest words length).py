text = "python programming is really intresting"

def longest_word(text):

    word = text.split()
    longest = word[0]

    for x in range(len(word)):

        if len(word[x]) > len(longest):

            longest = word[x]

    return len(longest)

result = longest_word(text)
print("the longest word length is :",result)
