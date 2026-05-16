# You will be given an array
# your task is to find the largest element from the given ArrayLike

# Example 1:
# input: [2,3,1,5,6,9]
# Ouput: 9

# Example 2:
# input: [1, 1, 1]
# output: 1

# Example 3:
# input: [5,11,2,3]
# Ouput: 11

# Approach 1: (Brute Force)
# first sort the entire ArrayLike in ascending order
# return the last element in the sorted ArrayLike

# Approach 2: (Optimized)
# traverse through the arraylike and update the max element
# set max to -inf


def findLargest(array: list) -> int:
    if not array:
        raise ValueError("List is empty")
    largest_element = float('-inf')

    for element in array:
        largest_element = max(largest_element, element)

    return largest_element

# print(findLargest([2,3,4,5,1,-3, -2]))