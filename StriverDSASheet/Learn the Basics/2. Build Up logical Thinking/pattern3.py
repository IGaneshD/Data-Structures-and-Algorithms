
class Solution:

    def printPattern(self, N):

        for i in range(N):

            for j in range(i+1):
                print(f"{j+1}", end="")
            
            print()


obj = Solution()

obj.printPattern(5)