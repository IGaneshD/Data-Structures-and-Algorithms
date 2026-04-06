# Implement linear search
# Complexity:
# Best Case: O(1)
# Average Case: O(n)
# Worst Case: O(n)

# Input: arr -> List or Tuple(or Any ArrayLike)

import traceback

class ElementNotFoundError(BaseException):
    pass


def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        raise ElementNotFoundError("Element Not found")



arr = [1,2,3,4,5,6]
try:
    index = linearSearch(arr, target=50) # o(n)
    print(f"Element Found at {index}")
except ElementNotFoundError as e:
    print(e)