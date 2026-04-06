# Bubble Sort
# Sort an ArrayLike in ascending or descending order
# Complexity
# Best Case: O(n) - if array is already sorted
# Average Case: O(n^2)
# Worst Case: O(n^2)


class Solution:

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        # code goes here
        n = len(self.arr)
        for i in range(n):
            flag = True # optimized approach
            # print(f"{i+1}th Iteration")
            for j in range(n-i-1):
                if self.arr[j]>self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    flag = False
            # print(self.arr)
            if flag:
                break


arr = [5, 4, 3, 2, 1]
# arr = [1,2,3,4,5]
obj = Solution(arr)
obj.sort()
print("Sorted List:", arr)