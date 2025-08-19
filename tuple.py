my_tuple=("jocker","harley","batman","catwoman")
print(my_tuple)
# del(my_tuple)
# print(my_tuple)

# update by reassigning
# my_tuple=(1,2,3)
# print(my_tuple)

#update by converting to list
# list1=list(my_tuple)
# list1[3]='sagar'
# my_tuple=tuple(list1)
# print(my_tuple)

# tuple2=("spiderman","superman","shaktiman")
# tuple3=my_tuple+tuple2
# print(tuple3)

# print(my_tuple.count("catwoman"))
# print(my_tuple.index("batman"))

# (var1,var2,var3,var4)=my_tuple
(var1,*var2,var3)=my_tuple
print(var1)
print(var2)
print(var3)
# print(var4)
