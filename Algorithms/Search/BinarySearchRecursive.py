
def RecursiveBinarySearch(arr, start, end , target) -> int | bool:
    if start > end: 
        return False
    
    mid = start + (end - start)//2

    if arr[mid] == target:
        return mid
    
    if arr[mid] < target:
        return RecursiveBinarySearch(arr, mid+1, end, target)
    
    return RecursiveBinarySearch(arr, start, end-1, target)



arr = [1, 2, 3, 4, 5, 6, 7]
target = 10
result = RecursiveBinarySearch(arr, 0, len(arr)-1, target)
if result:
    print(f"{target=} found at index {result}")
    exit(1)

print(f"{target=} was not found")