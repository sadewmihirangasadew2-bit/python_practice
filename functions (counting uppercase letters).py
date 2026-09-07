text = "HELLO world"

def count(text):

    count = 0

    for x in range(len(text)):

        if text[x].isupper():

            count = count + 1

    return count

result = count(text)
print("number of uppercase letters are :",result)
