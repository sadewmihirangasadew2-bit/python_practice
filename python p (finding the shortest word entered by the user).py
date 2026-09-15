search = input("enter your word :")

def shortest_word(search):

    word = search.split()
    shortest = word[0]

    for x in range(len(word)):

        if len(word[x])< len(shortest):

            shortest = word[x]

    return shortest

result = shortest_word(search)
print("the shortest word is :",result)
