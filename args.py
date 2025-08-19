def sum(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
result=sum(1,44,5.5,33,9)
print(result)

def dict(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
dict(name="liya",age=23,gender="female")

def both(param1,*args,**kwargs):
    print("regular parameter",param1)
    print("arbitary arguments",args)
    print("keyword arguments",kwargs)
both(1,2,44,name="liya",DEPT="IT")
