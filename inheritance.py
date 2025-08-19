#single inheritance
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(f"{self.name}makes a sound")
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} makes a sound woof")
# dog=Dog("itatchi")
# dog.speak()
        
#multiple inheritance
# class Engine:
#     def start_engine(self):
#         print("engine is starting")
# class Wheel:
#     def rotate(self):
#         print("wheel is rotating")
# class Drive(Engine,Wheel):
#     def drive(self):
#         print("ready to drive")
# car=Drive()
# car.start_engine()
# car.rotate()
# car.drive()
    
#hierarchical inheritance
# class Animal:
#     def speak(self):
#         print("animal speaks")   
# class Dog(Animal):
#      def speak(self):
#         print("dogs be like woof,woof!")
# class Cat(Animal):
#     def speak(self):
#         print("cats be like meow meow!")
# car=Cat()
# dog=Dog()
# car.speak()
# dog.speak()

#ducktype
# class Dog:
#     def speak(Self):
#          print("dogs be like woof,woof!")
# class Cat:
#       def speak(Self):
#          print("cats be like meow!")
# class cow:
#      def moo(self):
#           print("moo moo!")
# def make_noise(animal):
#     try:
#         animal.speak()
#     except AttributeError:
#         print("cow one doesnt work because of different class name...")
# cat=Cat()
# dog=Dog()
# cow=cow()
# make_noise(cat)
# make_noise(dog)
# make_noise(cow)


