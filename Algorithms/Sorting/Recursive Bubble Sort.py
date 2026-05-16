def recursive_bubble_sort(arr, i, j, end, flag):
    if j == end - i - 1:
        return flag
    if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        flag = True
    print(arr, i, flag)
    return recursive_bubble_sort(arr, i, j+1, end, flag)

arr = list(map(int, input("Enter an array: ").split()))

for i in range(len(arr)):
   swapped_flag = recursive_bubble_sort(arr, i, 0, len(arr), False)
   if not swapped_flag:
       break

print(arr)