text = "python programming is really fun"

def longest_word(text):

    words = text.split()
    longest = words[0]

    for x in range(len(words)):

        if len(words[x])> len(longest):

            longest = words[x]
            
    return longest

result = longest_word(text)
print("longest word is :",result)

        

        
