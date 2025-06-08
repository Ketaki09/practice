# Reverse letters in words
words = "I am iron man"
def reverse_method(words):
    reverse_word = words.split()
    output = []
    
    for each in reverse_word:
        output.append(each[::-1])
    
    return ' '.join(output)
    

print(reverse_method(words))