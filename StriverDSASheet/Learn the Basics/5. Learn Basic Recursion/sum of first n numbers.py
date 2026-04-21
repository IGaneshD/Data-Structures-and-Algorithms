
# def sum_of_first_n_numbers(current_number, N):
#     if current_number == N:
#         return current_number
    
#     return current_number + sum_of_first_n_numbers(current_number+1, N)


# print(sum_of_first_n_numbers(1, 11))

def sum_of_first_n_numbers(N):
    if  N == 1:
        return 1
    
    return N + sum_of_first_n_numbers(N-1)

N = int(input("Enter N:"))

while N < 1:
    N = int(input("Enter N(should be +ve integer):"))
print(sum_of_first_n_numbers(N))
