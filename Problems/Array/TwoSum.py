


class Solution:

    def twoSum(self, arr, target):
        
        n = len(arr)

        hashmap = {arr[i]:i for i in range(n)}

        for i in range(n):
            complement = target - arr[i]

            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        
        return []



obj = Solution()

print(obj.twoSum(arr=[2,7,11,15], target=14))
