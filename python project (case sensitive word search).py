text = "python is fun and python is easy and PYTHON is powerful"

search = input("enter the word :")

def word_search(text,search):
    
    count = 0
    word = text.split()

    for x in range(len(word)):

        if  word[x].lower()== search.lower():

            count = count + 1

    return count

result = word_search(text,search)
print(search,"has appeared",result,"times")
