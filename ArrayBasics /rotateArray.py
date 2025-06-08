#In this variation, you will be receiving an array of Int, where the number 0 represents a word break. Reverse all the elements between the 0s.
#Ex. [1, 2, 3, 0, 4, 5, 6] returns [3, 2, 1, 0, 6, 5, 4] (1, 2, 3 and 4, 5, 6 were the two chunks that were reversed)
#Ex. [1, 2, 3, 4, 5, 6] returns [6, 5, 4, 3, 2, 1] (since there are no zeroes, the entire array is considered one chunk)
#x. [1, 0, 2, 0, 3] returns [1, 0, 2, 0, 3] (Since all the chunks size 1, no change happens)

def reverse_chunks(arr):
    result = []
    chunk = []
    
    for num in arr:
        if num == 0:
            # Process the current chunk
            if len(chunk) > 1:
                result.extend(chunk[::-1])
            else:
                result.extend(chunk)
            # Add the 0 itself
            result.append(0)
            # Reset chunk
            chunk = []
        else:
            chunk.append(num)
    
    # Process the last chunk (after the last 0, or whole array if no 0)
    # if len(chunk) > 1:
    result.extend(chunk[::-1])
    # else:
        # result.extend(chunk)
    
    return result

# Test cases
print(reverse_chunks([1, 2, 3, 0, 4, 5, 6,7]))  # [3, 2, 1, 0, 6, 5, 4]
