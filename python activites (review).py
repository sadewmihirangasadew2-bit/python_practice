search = input("enter your sentence :")

walmart = input("enter your letter :")

def count_end(search,walmart):

    word = search.split()
    count = 0

    for x in range(len(word)):

        if word[x][-1].lower() == walmart.lower():

            count = count + 1

    return count

result = count_end(search,walmart)
print("words ending with",walmart,":",result)
