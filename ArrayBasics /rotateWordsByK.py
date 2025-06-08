# Rotate words by x
# In this variation we will rotating the words by k positions. If k = 1, move all words 1 to the right and the last word should move to the beginning.
#Ex. “Rotate the words in this string”, k = 1 returns “string Rotate the words in this”
#Ex. “Rotate the words in this string”, k = 2 returns “this string Rotate the words in”
#Ex. “Rotate the words in this string”, k = 3 returns “in this string Rotate the words”
#Ex. “Rotate the words in this string”, k = 6 returns “Rotate the words in this string”
#Ex. “Rotate the words in this string”, k = 7 returns “this string Rotate the words in”
sentence = "Luke, I am your father!"

def rotate_by_k(sentence,k):
    word = sentence.split()
    n = len(word)

    #modulo check
    k = k % n 

    output = word[n-k:] + word[:n-k]

    return ' '.join(output)

print(rotate_by_k(sentence,2))