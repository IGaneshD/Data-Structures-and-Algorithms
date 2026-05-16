# Find the second largest element
# Approaches Could be:
# 1. Use Quick sort and find second largest element
# 2. using bubble sort and iterate for two times and return second largest element (fails for duplicate elmeents)
# 3. use two for loops, first will find the first maximum and second will find the second maximum

# Edge cases two deal with:
# 1. array has duplicate elements
# 2. array is empty
# 3. array have no second maximum element

# How can we address, if have duplicate elements
# -> one approach could be, first find all distinct elements and then we can find the second max element
# -> one apprach could be, use extra space like array of size k. each time is will have k max elements from the array we have traversed


# Ignore the edge cases

# approach 1
def secondLargestElementBruteForce(array):
    if len(array) < 2:
        return -1
    for i in range(2):
        
        for j in range(0, len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array[-2]


print(secondLargestElementBruteForce([1,2,3,0, 9, 8, 9]))

    

