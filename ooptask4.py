#7
# class Movie:
#     def __init__(self,title,available_seat):
#         self.title=title
#         self.available_seat=available_seat
#     def book_ticket(self,seats):
#         if(seats>self.available_seat):
#             print("not enough seats")
#         else:
#             print(f"{seats} seats booked successfully")
#             self.available_seat=self.available_seat-seats
# title=input("enter the movie title: ")
# available_seat=int(input("enter available seats"))
# mov=Movie(title,available_seat)
# for i in range(3):
#     seats=int(input("enter seats to book: "))
#     mov.book_ticket(seats)


# #8
# class Loan:
#     def __init__(self,name,income,credit_score):
#         self.name=name
#         self.income=income
#         self.credit_score=credit_score
#     def check_eligibility(self):
#         if(self.income>=25000 and self.credit_score>=650):
#             print(f"{self.name} is eligible for loan")
#         else:
#             print(f"{self.name} is not eligible for loan")
# name=input("enter the name ")
# income=float(input("enter the income "))
# credit=float(input("enter the credit score "))
# obj=Loan(name,income,credit)
# obj.check_eligibility()

#9
class Order:
    def __init__(self,order_id,pro_name,status):
        self.order_id=order_id
        self.pro_name=pro_name
        self.status=status
    def __str__(self):
        return(f"order id:{self.order_id}\nstatus:{self.status}")
class ordertrack:
    def __init__(self):
        self.orders=[]
    def add_order(self):
        order_id=input("enter the id:")
        pro_name=input("enter the product name:")
        status=input("enter the status:")
        order=Order(order_id,pro_name,status)
        self.orders.append(order)
    def update_order(self):
        order_id=input("enter id to update status: ")
        for order in self.orders:
            if order.order_id==order_id:
                order.status=input("enter the new status:")
                print("order status updated")
                return
            else:
                print("order not found...enter the correct id")
    def display(self):
        for order in self.orders:
            print(order)
tracker=ordertrack()
num_orders=int(input("enter the no.of orders to add: "))
for i in range(num_orders):
    tracker.add_order()
while True:
    print("1-update status")
    print("2-display orders")
    print("3-exit")
    choice=input("enter the choice")
    if choice=="1":
        tracker.update_order()
    elif choice=="2":
        tracker.display()
    elif choice=="3":
        break
    else:
        print("invalid choice")
# tracker.display()


