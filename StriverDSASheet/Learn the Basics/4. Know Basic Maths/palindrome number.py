
class Solution:

    ## -------- Approach 1 ---------- ##
    ## -------- Naive Approach ------ ##
    def CheckPalindromeNumber1(self, num):

        if num < 0:
            return False
        original_number = num
        reversed_number = 0

        while num:
            rem = num % 10
            reversed_number = reversed_number * 10 + rem
            num //=10
        
        return reversed_number == original_number
    
    
    ## -------- Approach 2 ---------- ##
    ## --- better than approach 1 --- ##
    def CheckPalindromeNumber2(self, num):

        if num < 0 or (num % 10 and num != 0):
            return False
        
        reversed_number = 0

        while num > reversed_number:
            reversed_number = reversed_number * 10 + num % 10
            num //=10
        
        return reversed_number == num or num == reversed_number // 10


solution = Solution()

print(solution.CheckPalindromeNumber(-121)) # Negative numbers are not considered as palindrome
print(solution.CheckPalindromeNumber(0))
print(solution.CheckPalindromeNumber(121))
