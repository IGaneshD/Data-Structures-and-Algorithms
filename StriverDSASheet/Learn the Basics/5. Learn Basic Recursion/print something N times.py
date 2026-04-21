# import sys

# sys.setrecursionlimit(100) # Default is 1000

def print_n_times(name, i):
    # if not i:
    #     return
    print(name)
    print_n_times(name, i-1)


print_n_times("Ganesh", 10)