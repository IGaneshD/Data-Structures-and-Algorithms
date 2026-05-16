# Quick sort Algorithm for sorting
# It has Time Complexity
# Best Case: O(n logn)
# Average Case: O(n logn)
# Worst Case: O(n log)

# This is a divide and conquer algorithm 
# we choose an element as an pivot and try to find it correct position in given array
# we repeat the same for subarrays until element in the subarray is one
# this pivot element could be first element, last element or random element in subarray
# Generally we use this algorithm to sort large datasets or ArrayLike.
# we can use quick sort for finding the nth largest element in the array

# Pseudo Code:
# 1.Take an array as an input.
# 2.repeat this until subarray have one element
# 2.1.find piviot's position in the array, such that all element smaller than pivot will be on left of it and bigger on right side
# 2.2.recurse this function for left side of the pivot element
# 2.3 recurse this function for right side of the pivot element

# Psuedo Code to get pivot elements index(Let's call this function as partition(arr, start, end))
# 1. set i, j = start - 1, start
# 2. set the arr[end] as pivot
# 3. repeat for j = start to end -1
# 3.1 IF arr[j] smaller than pivot 
# 3.1.1 set i += 1 and swap arr[i] and arr[j]
# 4. set i+= 1 and swap arr[i] and arr[end]
# 5. return the i (this index is the correct position of pivot so we can split the arrays into two parts)



def partition(arr, start, end):
    i , j = start - 1 , start
    pivot = arr[end]
    while j <= end:
        if arr[j] <= pivot:
            i += 1
            # swap the ith and jth elements
            arr[i], arr[j] = arr[j], arr[i]

        j += 1
    
    return i



def QuickSort(arr, start, end):
    
    # # repeat while number of elements in subarray is one
    # print(arr, start, end)
    # if start < end:
    #     # get the position of pivot element
    #     pi = partition(arr, start, end)
    #     # divide the array into subarrays based on pivot elements index
    #     QuickSort(arr, start, pi-1)
    #     QuickSort(arr, pi + 1, end)

    # Tail call optimization with just one recursive call
    while start < end:
        pi = partition(arr, start, end )

        QuickSort(arr, start, pi - 1)

        start = pi + 1




# arr = [10, 3, 4, 2, 1, 90, 0, 34, 45, 33, 56]
arr = [10, 3, 4, 2, 1, 90, 0]
print(f"Array befor Sorting: {arr=}")
QuickSort(arr, 0, len(arr)-1)
print(f"Array after Sorting: {arr=}")