class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary  #private
    def display(self):
        print(f"name:{self.name}\nsalary:{self.__salary}")
    def update_salary(self,new_salary):
        self.__salary=new_salary

emp=Employee("liya",60000)
emp.display()

emp.name="nashith"
emp.update_salary(80000)
emp.display()