

class Solution:
    
    def printPattern(self, number):
        
        for i in range(number):
            print(f"{i+1}"*(i+1))


solution = Solution()
solution.printPattern(5)