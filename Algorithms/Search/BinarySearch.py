# Binary Search
# searches for value with O(logn)
# Time Complexity:
# Best Case : O(1)
# Average Case: O(logn)
# Worst Case: O(logn)
# This uses Divide and Conqure

# NOTE: array should be sorted, if not sort it first

# Peusdo Code:
# function Binary Search:
# set low = 0, high = n-1
# calculate mid = low + (high - low)// 2
# if arr[mid] is target return index
# if arr[mid]< target then set low = mid + 1
# if arr[mid]> target then set high = mid - 1
# repeat until low < high




def BinarySearch(arr, target)-> int | bool:
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + ( high - low )//2
        if arr[mid] == target:
            return mid
        if arr[mid]<target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False



arr = [10, 11, 15, 18, 21, 25]
result = BinarySearch(arr, target=17)
if not result:
    print("Element not present in List")
else:
    print(f"Element found at index {result}")