# Selection Sort
# Time Complexity(Comparisons):
# Best Case: O(n^2)
# Average Case: O(n^2)
# Worst Case: O(n)
# for swap: o(n)
# space complexity: O(1)


class Solution:

    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
    

    def sort(self):

        for i in range(self.n-1):
            
            minIndex = i
            # print(f"Iteration {i+1}")
            for j in range(i+1, self.n):
                
                if self.arr[j] < self.arr[minIndex]:
                    minIndex = j
            
            if i != minIndex:
                self.arr[i], self.arr[minIndex] = self.arr[minIndex], self.arr[i]
    
            # print(self.arr)

selectionSort = Solution([8,9,7,6,5,4])
selectionSort.sort()
print(selectionSort.arr)
        