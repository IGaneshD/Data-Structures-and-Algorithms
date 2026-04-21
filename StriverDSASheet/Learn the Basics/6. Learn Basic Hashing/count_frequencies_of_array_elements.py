from collections import defaultdict

# provides a default value for a key that does not yet exists, prevents KeyError Exception

hashmap = defaultdict(int)
nums = [1,2,2,1,3]

for num in nums:
    hashmap[num] += 1

print([list(item) for item in hashmap.items()])