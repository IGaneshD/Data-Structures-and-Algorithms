# Count all Digits of a Number
# Input: 150
# Ouput: 3
# Input: 1345
# Ouput: 1567


class Solution:


    def countDigits(self, number):
        
        count = 0

        while number:
            count += 1
            number = number // 10

        return count
    

sol = Solution()

print(sol.countDigits(123))
