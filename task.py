a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("choose operator\n1-add,2-sub,3-mult,4-div"))

if(c==1):
    print(a+b)
elif(c==2):
    print(a-b)
elif(c==3):
    print(a*b)
elif(c==4):
    if(b==0):
        print("division by zero is not possible")
    else:
        print(a/b)
else:
    print("invalid choice")


