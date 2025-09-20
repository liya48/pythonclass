a= input("Enter first word: ")
b= input("Enter second word: ")

str1=a.replace(" ", "").lower()
str2=b.replace(" ", "").lower()


if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not an anagram")


# def missing_no(nums):
#     n=max(nums)
#     full_set=set(range(1,n+1))
#     actual_set=set(nums)
#     return sorted(list(full_set-actual_set))
# nums=[2,4,7,1]
# missing_number=missing_no(nums)
# print("the missing numbers are",missing_number)


                  


  


      