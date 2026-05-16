

def merge(arr, start, mid, end):
    LA = arr[start:mid+1]
    RA = arr[mid+1:end+1]
    # print(f"{LA=}, {RA=}")
    i = j = 0
    k = start
    n1 = len(LA)
    n2 = len(RA)

    while i<n1 and j<n2:
        if LA[i] < RA[j]:
            arr[k] = LA[i]
            i += 1
        else:
            arr[k] = RA[j]
            j += 1

        k += 1
    
    while i<n1:
        arr[k] = LA[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = RA[j]
        j += 1
        k += 1


def sort(arr):
    arr_len = len(arr)
    current_size = 1 # size of single subarray

    while current_size < arr_len:
        leftEnd  = 0

        while leftEnd < arr_len:

            mid = min(leftEnd + current_size - 1, arr_len - 1)
            rightEnd = min(leftEnd + current_size * 2 - 1, arr_len-1)

            merge(arr, leftEnd, mid, rightEnd)
            leftEnd += 2 * current_size
        
        current_size *= 2
    
    return arr



arr = [5, 1, 3, 4, 10, 9, 8]
sort(arr)
print(arr)