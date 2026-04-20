# Problem:
# You will be given a interger number, you have to find if the given number
# is a prerfect square
# if yes, return True, otherwise False
# 1=<num<n

# NOTE: you are not allowed to use inbuilt functions like `sqrt`

def isPerfectSquare(num: int) -> bool:
        low = 1
        high = num

        while low <= high:
            mid = low + (high - low)//2
            if mid**2 == num:
                return True
            if mid**2 > num : high = mid - 1
            else: low = mid + 1

        return False


