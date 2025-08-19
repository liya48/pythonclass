# a=int(input("enter the number"))

# digit2=a
# sum=0
# while(digit2>0):
#     digit=digit2%10
#     sum=sum+(digit**3)
#     digit2=digit2//10

# if(sum==a):
#     print(f"{a} is armstrong")
# else:
#     print("not an armstrong")

def missing_number(nums):
    nums = list(nums)  
    n = max(nums) 
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

a = {1, 2, 3, 4, 6}
print("Missing number:", missing_number(a))

