# Given an array of positive integers, find the first element that occurs k number of times. If no element occurs k times, return -1. You may assume k is greater than 0.
# Examples:
# • Given an array: [1, 2, 2, 3, 3], k: 2 // returns 2
# • Given an array: [], k: 1 // returns -1
# The standard solution is to use a dictionary to keep track of the number of repetitions. Early return when you find an element that hits k repeats.
# The original solution, but do not return early. Build up the full dictionary of counts. Iterate through the array again and return the first one whose count is greater than or equal to k. Discuss how this does not change the overall runtime or space complexity.
# For each element, iterate through the rest of the array to see if it's repeated k times. If it is, return it. Otherwise, go on to the next element. Walk through how this approach is O(n^2) runtime.
# Extra problems if there is time:
# How many distinct values occur exactly k times?
# How many distinct values occur at minimum k times?
# Find the mininum value that occurs at least k times?
# Find the mode. Recall the mode is the most frequently occurring value?

def first_to_k_elements(arr,k):
    solution = -1
    hashMap = {}
    finalSet = set()
    if arr == []:
        return solution
    
    for element in arr:
        if element in hashMap:
            hashMap[element] = hashMap.get(element,0) + 1  
            print(hashMap)
            # if hashMap[element] == k:
            #     return element
        else:
            # hashMap.update(element:1)
            hashMap[element] = 1
    
    # for element in arr:
    #     if hashMap[element] >= k:
    #         return element
    
    for element in arr:
        if hashMap[element] == k:
            finalSet.add(element)
            print(finalSet)
        if hashMap[element] >= k:
            finalSet.add(element)
            print(finalSet)
    print(hashMap)
    return solution

print(first_to_k_elements([1, 2, 2, 3, 3,4,4,4],2))