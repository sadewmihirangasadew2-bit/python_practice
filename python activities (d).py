letter = input("enter your sentence :")

mark = input("enter your letter :")

def count_starting(letter,mark):

    word = letter.split()
    count = 0

    for x in range(len(word)):

        if word[x][0].lower() == mark.lower():

            count = count + 1

    return count

result = count_starting(letter,mark)
print("the result is :",result)
