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

        print(f"{countArray=}")
        # for i in range(len(countArray)):
        #     for j in range(countArray[i-1], countArray[i]):
        #         arr[j] = i

        # tempArray = [0]*size
        # i = 0
        # while i < size:
        #     tempArray[countArray[arr[i]]-1] = arr[i]
        #     countArray[arr[i]] -= 1
        #     i += 1
        
        # print(tempArray)

        for i in range(len(countArray)):
            if i != 0:
                self.fill(arr, countArray[i-1], countArray[i], i)
            else:
                self.fill(arr, 0, countArray[i], i)
        
        print(f"{arr=}")

    def fill(self, arr, start, end, element):
        
        for i in range(start, end):
            arr[i] = element




arr = [0,0,3,3,3,1,1,1,1,5,0,5,5,5,6,6,6,6]

obj = Solution()

obj.sort(arr)