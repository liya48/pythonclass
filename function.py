
# #positional argument
# def sum(num1,num2):
#     return(num1+num2)
# print(sum(2,3))

# #keyword  argument
# def biodata(name,age):
#     print(f"name:{name}")
#     print(f"age:{age}")
# biodata(age=22,name='liya')

# #default argument
# def biodata(age,name="liya"):
#     print(f"name:{name}")
#     print(f"age:{age}")
# biodata(age=13)

#docstring
# def sum(num1,num2):

#     """this adds two no.s"""
#     return(num1+num2)
# print(sum.__doc__)

#lambda function
# a=lambda a,b:a+b
# print(a(6,9))

#map(higher order fn)
num=[1,4,3,5]
squared=map(lambda a:a*a,num)
print(list(squared))

#filter
num=[1,4,3,6,8,33,22,0]
even=filter(lambda n:n%2==0,num)
print(list(even))

#reduce
from functools import reduce
num=[1,3,4,6,6]
sum=reduce(lambda x,y:x+y,num)
print(sum)

# def increment(n):
#     return lambda x:x+n
# increased=increment(5)
# print(increased(30))

# def sum(a,b):
#     return lambda a,b:a+b
# add=sum(3,6)
# print(add(1,2))

# x=10 #global variable
# def outer_fun():
#     x=7 #enclose variable
#     def inner_fun():
#         # x=3 #local var
#         print(x)
#     inner_fun()

# outer_fun()
