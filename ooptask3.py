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

# 4
class Book:
    def __init__(self,title,author,copies):
        self.title=title
        self.author=author
        self.copies=copies
    def display_info(self):
        print(f"TITLE:{self.title}\nAUTHOR:{self.author}\nCOPIES AVAILABLE:{self.copies}")
books=[]
for i in range(3):
    title=input("enter the book title:")
    author=input("enter author:")
    copies=int(input("enter copies:"))
    book=Book(title,author,copies)
    books.append(book)
search_title=input("enter title to search")
flag=0
for book in books:
    if (book.title.lower()==search_title.lower()):
        book.display_info()
        flag=1
        break
if flag==0:
    print("book not found")
    
