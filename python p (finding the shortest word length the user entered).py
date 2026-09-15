search = input("enter your sentence : ")

def shortest_word_length(search):

    word = search.split()
    shortest = word[0]

    for x in range(len(word)):

        if len(word[x])< len(shortest):

            shortest = word[x]

    return len(shortest)

result = shortest_word_length(search)
print("the shortest word length :",result)
