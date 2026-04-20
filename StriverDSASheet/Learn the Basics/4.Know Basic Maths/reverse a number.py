# Reverse a Number
# you will be given an interger
# Your job is to reverse a numbers without converting into string
# Example:
# input: 123
# output: 321
# input: 1300
# ouput: 31

class Solution:

    def reverseNumber(self, number):
        
        reversedNumber = 0

        while number:
            rem = number % 10
            reversedNumber = reversedNumber * 10 + rem
            number = number // 10
        
        return reversedNumber



obj = Solution()
print(obj.reverseNumber(123))
print(obj.reverseNumber(1300))