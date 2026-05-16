# Merge Sort
# Divide and Conqure Algorithm

def merge_and_sort(arr, start, mid, end):
    temp_1 = arr[start:mid+1]
    temp_2 = arr[mid+1:end+1]

    k = start
    len_of_temp_1 = len(temp_1)
    len_of_temp_2 = len(temp_2)
    i = j = 0

    while i<len_of_temp_1 and j<len_of_temp_2:
        if temp_1[i] < temp_2[j]:
            arr[k] = temp_1[i]
            i += 1
        else:
            arr[k] = temp_2[j]
            j += 1
        k += 1
    
    while i < len_of_temp_1:
        arr[k] = temp_1[i]
        k += 1
        i += 1

    while j < len_of_temp_2:
        arr[k] = temp_2[j]
        k += 1
        j += 1

def divide(arr, start, end):
    print(f"{arr[start:end+1]}, {start=}, {end=}")
    if start==end:
        return
    mid = (start + end) // 2
    divide(arr, start, mid)
    divide(arr, mid+1, end)

    # sort and merge the array
    merge_and_sort(arr, start, mid, end)


def sort(arr):
    divide(arr, 0, len(arr)-1)
    print(arr)


sort([5, 1, 3, 4, 10, 9, 8])

