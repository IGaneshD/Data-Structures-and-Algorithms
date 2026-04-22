from collections import defaultdict


class Solution:

    def highestOccuringElement(self, array):

        # return -1 if array is empty
        # not possible because 1<= n <1000
        # if not array:
        #     return -1
        
        frequency_map = defaultdict(int)

        for num in array:
            frequency_map[num] += 1

        max_freq = -1 # stores maximum frequency count
        result = None # stores the most frequent num

        for num, freq in frequency_map.items():
            if freq > max_freq or (freq == max_freq  and num < result):
                max_freq = freq
                result = num
        
        return result
        
        # No need of sorting
        # sorted_frequency_map = sorted(frequency_map.items(), key=lambda x:(-x[1], x[0]))
        # return sorted_frequency_map[0][0]

solution =  Solution()
print(solution.highestOccuringElement([1,2,2,3]))
print(solution.highestOccuringElement([1,4,4,3,3,]))
print(solution.highestOccuringElement([]))