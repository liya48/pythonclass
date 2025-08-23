# str=input("enter the word to check:")
# length=len(str)
# right=length-1
# left=0
# flag=0
# while (left<=right):
#     if(str[right]==str[left]):
#         right=right-1
#         left=left+1
#     else:
#         flag=1
#         break
# if(flag==1):
#     print("not palindrome")
# else:
#     print("palindrome")



n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

