

def fact(n):
    if n==0:
        return 1
    
    return n * fact(n-1)

n = int(input("Enter Number > 0: "))

while not n:
    n = int(input("Enter Number > 0:"))

print(fact(n))