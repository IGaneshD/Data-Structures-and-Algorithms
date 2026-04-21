def printNumbers(end, number=1):
    if number > end:
        return
    print(number, end=" ")
    printNumbers(end, number+1)


printNumbers(100)