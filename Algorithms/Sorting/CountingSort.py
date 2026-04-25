# Counting Sort
# This sorting algorithm is used for sorting elements with multiple occurences
# Time Complexity:
# Best Case: O(N+M)
# Worst Case: O(N+M)
# Average Case: o(N+M)


class Solution:

    def sort(self, arr):

        size = len(arr)

        max_element = max(arr)
        countArray = [0]*(max_element + 1)

        # count the occurences of the element in store them in countArray[element]
        for element in arr:
            countArray[element] += 1
        
        # do the cumilative addition of occurences in countArray
        for i in range(1,len(countArray)):
            countArray[i] += countArray[i-1]

        # print(f"{countArray=}")

        tempArray = [0]*size
        i = 0
        while i < size:
            tempArray[countArray[arr[i]]-1] = arr[i]
            countArray[arr[i]] -= 1
            i += 1
        
        arr = tempArray

        return arr


arr = [0,0,3,3,3,1,1,1,1,5,0,5,5,5,6,6,6,6]

obj = Solution()

print(obj.sort(arr))
