# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# def tail_recursion(n,accumulator=1):
#     if n==0 or n==1:
#         return accumulator
#     else:
#         return tail_recursion(n-1,accumulator*n)
# print(tail_recursion(5))

# fact=1
# for i in range (1,6):
#     fact=fact*i
# print(fact)

# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return (fib(n-1)+fib(n-2))
    
# print(fib(8))

# def sum_list(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0]+sum_list(lst[1:])
# print(sum_list([1,2,3,6,5]))
    