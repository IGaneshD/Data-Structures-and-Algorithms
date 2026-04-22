
def solution(N):

    for i in range(N):
        for j in range(0, i+1):
            print("*", end="")
        print("", end="\n")


solution(10)