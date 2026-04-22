
class Solution:

    def printReverseRightTringle(self, size):
        
        for i in range(size):
            print("*"*(size-i))


solution = Solution()
solution.printReverseRightTringle(5)