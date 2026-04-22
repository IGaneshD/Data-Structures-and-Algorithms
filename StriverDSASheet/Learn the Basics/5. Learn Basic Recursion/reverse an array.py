def reverseArray(arr, i, j):
    if i>=j:
        return
    
    arr[i], arr[j] = arr[j], arr[i]
    
    return reverseArray(arr, i+1, j-1)

arr = [1,4,5,1,2,3]
print(f"before {arr=}")
reverseArray(arr, 0, len(arr)-1)
print(f"after {arr=}")

