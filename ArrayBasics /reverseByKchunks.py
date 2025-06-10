def reverse_in_k_chunks(s, k):
    result = []
    for i in range(0, len(s), k):
        chunk = s[i:i+k]
        result.append(chunk[::-1])  # Reverse each chunk
    return ''.join(result)


print(reverse_in_k_chunks("here",2))