search = input("enter your sentence :")

def count_vowels(search):

    count = 0

    for x in range(len(search)):

        if search[x]  in "aeiou":

            count = count + 1

    return count

result = count_vowels(search)
print("number of vowels are :",result)
    
