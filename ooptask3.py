# class Bird:
#     def sound(self):
#         print("Bird makes a sound")
# class Parrot(Bird):
#     def sound(self):
#         print("parrot says hello")
# class Sparrow(Bird):
#     def sound(self):
#         print("sparrow chirps")
# def make_sound(bird):
#     bird.sound()
# parrot=Parrot()
# sparrow=Sparrow()
# make_sound(parrot)
# make_sound(sparrow)

#4
class Book:
    def __init__(self,title,author,copies):
        self.title=title
        self.author=author
        self.copies=copies
    def display_info(self):
        print(f"TITLE:{self.title}\nAUTHOR:{self.author}\nCOPIES AVAILABLE:{self.copies}")
    