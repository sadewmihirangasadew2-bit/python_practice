text = "hello123world45"

def count(text):

    count = 0

    for x in range(len(text)):

        if text[x].isdigit():

            count = count + 1

    return count

result = count(text)
print("number of digits are :",result)
