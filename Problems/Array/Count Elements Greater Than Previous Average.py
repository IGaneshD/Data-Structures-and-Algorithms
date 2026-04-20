responseTimes = [100,120,150, 300]

average = 0
n = len(responseTimes)
count = 0
for i in range(0, n):
    average = (average *i + responseTimes[i])//(i+1)
    
    if responseTimes[i] > average:
        count += 1

print(f"{count=}")
# return count