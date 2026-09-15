search = input("enter your sentence :")

def longest_word(search):

    word = search.split()
    longest = word[0]

    for x in range(len(word)):

        if  len(word[x])> len(longest):

            longest = word[x]

    return longest

result = longest_word(search)
print("the longest word is :",result)
