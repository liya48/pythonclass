class Student:
    def __init__(self,name,mark):
       self.name=name
       self.mark=mark
    def display_grade(self):
        print(f"NAME: {self.name}")
        if(self.mark>=90):
            print("GRADE: A")
        elif(self.mark>=75):
            print("GRADE: B")
        elif(self.mark>=50):
            print("GRADE: C")
        else:
            print("FAIL")
stu1=Student("deepthi",50)
stu1.display_grade()

stu2=Student("Aleyna",75)
stu2.display_grade()

stu3=Student("Adam",40)
stu3.display_grade()

