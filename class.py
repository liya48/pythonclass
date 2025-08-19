#with constructor
# class Car:
#     def __init__(self,model,price):
#         self.model=model
#         self.price=price
#     def feature(self):
#         print(f"Model:{self.model}\nPrice:{self.price}")

# car1=Car("Range Rover Velar","Rs. 84.90 Lakh")
# car2=Car("Mustang GT Fastback","Rs.74.61 Lakh")
# car1.feature()
# car2.feature()
# car1.model="Mercedes-Benz E-Class"  #upodating value
# car1.feature()


#without constructor
# class student:
#     def ReadDetails(self,name,Dept,year):
#         self.name=name
#         self.dept=Dept
#         self.year=year
#     def printdetails(self):
#         print(f"Name:{self.name}\nDepartment:{self.dept}\nYear:{self.year}")

# stu1=student()
# stu1.ReadDetails("Liya","Bsc IT","3rd year")
# stu1.printdetails()

# stu2=student()
# stu2.ReadDetails("Nashith","M Tech","4th year")
# stu2.printdetails()

# stu2.dept="B Tech"  #reaasigning
# stu2.printdetails()
# print(stu2.year)   #accessing attribute

#loosely coupled composition
# class company:
#     def __init__(self,name,place):
#         self.name=name
#         self.place=place

# class employee:
#     def __init__(self,name,age,comp:company):
#         self.name=name
#         self.age=age
#         self.comp=comp
#     def printdetails(self):
#         print(f"name:{self.name}\nage={self.age}\ncompanyName:{self.comp.name}\ncompanyPlace:{self.comp.place}")

# #person1=employee("liya","23", company("wipro","banglore"))
# #or
# company1 = company("Wipro", "Bangalore")
# person1 = employee("Liya", 23, company1)
# person1.printdetails()

#tightly coupled composition
# class company:
#     def __init__(self,name,place):
#         self.Cname=name
#         self.place=place

# class employee:
#     def __init__(self,name,age,Cname,place):
#         self.name=name
#         self.age=age
#         self.company = company(Cname, place)
#     def printdetails(self):
#         print(f"name:{self.name}\nage:{self.age}\ncompanyName:{self.company.Cname}\ncompanyPlace:{self.company.place}")
# person1=employee("liya","23","wipro","banglore")
# person1.printdetails()

# #inner class
# class Company:
#     class employee:
#         def __init__(self,name,place):
#             self.Cname=name
#             self.place=place

#     def __init__(self,name,age,Cname,place):
#         self.name=name
#         self.age=age
#         self.company =Company.employee(Cname, place)
#     def printdetails(self):
#         print(f"name:{self.name}\nage:{self.age}\ncompanyName:{self.company.Cname}\ncompanyPlace:{self.company.place}")

# person1=Company("liya","23","wipro","banglore")
# person1.printdetails()
        
#static method
# class MathOperation:
#     @staticmethod
#     def sum(a,b):
#         return(a+b)
# print(MathOperation.sum(10,29))
class Company:
    company="abc"
    @classmethod
    def change_comp(cls,cname):
        cls.company=cname

    def __init__(self,name,place):
        self.name=name
        self.place = place


        def printdetails(self):
            print(f"name: {self.name}")
            print(f"age: {self.age}")
           
           
per1=Company("john","fgh")
per2=Company("fghj","sdfghjk")
print(per1.company)
print(per2.company)

per1.change_comp("zxcvbnm")
print(per1.company)
print(per2.company)


