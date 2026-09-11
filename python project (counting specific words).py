text = "python is fun and python is easy and python is powerful"

def count(text):

    count = 0
    word =text.split()

    for x in range(len(word)):

        if word[x]== "python":

            count = count + 1

    return count

result = count(text)
print("python appears :",result,"times")
