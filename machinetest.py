class FoodItem:
    def __init__(self,item_id,name,price):
        self.item_id=item_id
        self.name=name
        self.price=price
    def display_info(self):
        print(f"ID:{self.item_id},Name:{self.name},Price:Rs{self.price}")

class Order:
    def __init__(self):
        self.cart={}
    def add_item(self,food_item,quantity):
        if food_item.item_id in self.cart:
            self.cart[food_item.item_id]['quantity']+=quantity
        else:
            self.cart[food_item.item_id]={'item':food_item,'quantity':quantity}
    def remove_item(self,item_id):
        if item_id in self.cart:
            del self.cart[item_id]
        else:
            print("item not found in cart")
    def calculate_total(self):
        total=sum(item['item'].price*item['quantity']for item in self.cart.values())
        return total
    def display_order(self):
        for item_id,item in self.cart.items():
            print(f"{item['item'].name}x{item ['quantity']}=Rs {item['item'].price*item['quantity']}")
        print(f"Total:Rs{self.calculate_total()}")
menu= [
      FoodItem(1,'pizza',150),
      FoodItem(2,'Burger',150),
      FoodItem(3,'Sandwitch',80),
      FoodItem(4,'Fries',60),
      FoodItem(5,'coke',40)
      ]
Order=Order()
while True:
    print("\nFoodmenu")
    for items in menu:
        items.display_info()
    print("\n1-Add item to cart")
    print("\n2-Remove item from cart")
    print("\n3-View cart")
    print("\n4-checkout")

    choice=input("enter choices: ")

    if choice=='1':
       item_id=int(input("enter item ID to add:"))
       quantity=int(input("enter quantity"))
       item_to_add=next((item for item in menu if item.item_id==item_id),None)
       if item_to_add:
           Order.add_item(item_to_add,quantity)
           print(f"{item_to_add.name} added to cart")
       else:
           print("invalid item ID")
    elif choice=='2':
        item_id=int(input("enter the item ID to remove: "))
        Order.remove_item(item_id)
    elif choice=='3':
        Order.display_order()
    elif choice=='4':
        Order.display_order()
        print("thank u for ordering!")
        break
    else:
        print("invalid choice,pls try again.")

           