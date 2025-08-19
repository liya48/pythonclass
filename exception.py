# try:
#     num=10/0
# except ZeroDivisionError:
#     print("not possible")

# try:
#     a=int(input("enter a number"))
#     result=10/a
# except ZeroDivisionError:
#     print("0 not allowed") 
# else:
#     print(result)
# finally:
#     print("this is always executed")

# try:
#     a=int(input("enter a number"))
# except ValueError:
#     print("wrong datatype")
# else:
#     print("valid")
# finally:
#     print("thanks for your participation")

#custom error

# class NegativeNoError(Exception):
#     pass
# def check_num(num):
#     if num<0:
#         raise NegativeNoError("negative numbers are not allowed")
# try:
#     check_num(-1)
# except NegativeNoError as e:
#     print(e)


class NegativeNoError(Exception):
    pass
def check_num(num):
    if num<0:
        raise NegativeNoError("negative numbers are not allowed")
print(check_num(-10))