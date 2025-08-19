num=[1,2,3,4,5,6]
target=6
pairs=[]
for i in range(len(num)):
    for j in range(i,len(num)):
        if(i+j==target):
            pairs.append(f"({i},{j})")
print(pairs)

# a=int(input("enter the number"))



