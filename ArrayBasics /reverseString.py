# Reverse letters in words
# In this variation, keep the order of the words the same, but reverse the letters within each word.
words = "I am iron man"
def reverse_method(words):
    reverse_word = words.split()
    output = []
    
    for each in reverse_word:
        output.append(each[::-1])
    
    return ' '.join(output)
    

print(reverse_method(words))