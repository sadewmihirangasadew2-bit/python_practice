search = input("enter your sentence :")

def shortest_word(search):

    words = search.split()
    shortest = words[0]

    for x in range(len(words)):

        if len(words[x]) < len(shortest) :

            shortest = words[x]

    return shortest

result = shortest_word(search)
print("the shortest word is :",result)
