
class Solution:

    def printNumberTriangle(self, number):
        
        for i in range(number, 0, -1):
            for j in range(i):
                print(f"{j+1}", end="")
            print()

        # another solution
        # for i in range(number):

        #     for j in range(number-i):
        #         print(f"{j+1}", end="")
        #     print()



solution = Solution()
solution.printNumberTriangle(5)