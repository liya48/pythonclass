a=int(input("enter the size of array"))
my_list=[]
even_list=[]
odd_list=[]
sum=0
even_sum=0
odd_sum=0

for i in range(a):
    b=int(input(f"enter {a} elements"))
    my_list.append(b)
    if(b%2==0):
        even_list.append(b)
        even_sum=even_sum+b
    else:
        odd_list.append(b)
        odd_sum=odd_sum+b
    sum=sum+b
      

    
print(f"Even numbers in the list: {even_list}")
print(f"Odd numbers in the list: {odd_list}")
print(f"largest elements:{max(my_list)}")
print(f"sum of all elements:{sum}")
print(f"sum of even numbers:{even_sum}")
print(f"sum of even numbers:{odd_sum}")
print(f"count of even numbers:{len(even_list)}")
print(f"count odd numbers:{len(odd_list)}")









