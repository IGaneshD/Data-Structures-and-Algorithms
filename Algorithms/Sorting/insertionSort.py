# Insertion sort
# this is an efficient sorting algorithm becasue it iteratively finds the correct position of the element
# in the array and insert there.
# Time Complexity
# Best Case - O(n) - if the array is already sorted and number of elements in the list are n
# Average Case - O(n^2)
# Worst Case - O(n^2) - if the list is in reverse order

# Advantages 
# Space Efficient because of inplace algorithm
# Adoptive - the number of inversions is directly proportional to the number of swaps. no swapping happens if array is already sorted and it takes linear time O(n)

# Disadvantages
# inefficient for large lists
# Not as efficient as other sorting algorithms


class InsertionSort:

    def __init__(self, list):
        self.list = list

    
    def __call__(self):
        n = len(self.list)

        for i in range(n):
            temp = self.list[i]
            j = i
            while j>0 and temp<self.list[j-1]:
                self.list[j] = self.list[j-1]
                j -= 1
            
            self.list[j] = temp
            print(f"After {i=}, {self.list}")
        
        return self.list


sort = InsertionSort([10,1,5,11,2,13])

print(sort())