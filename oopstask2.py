class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    def deposit(self,deposit):
        self.__balance=deposit+self.__balance
    def withdraw(self,withdraw):
        if(withdraw<=self.__balance):
            self.__balance=self.__balance-withdraw
        else:
            print("not sufficient money")
    def get_balance(self):
        print(f"Name:{self.owner}")
        print(f"current balance:{self.__balance}")
per1=BankAccount("Alice",1000)
per1.deposit(100)
per1.withdraw(1200)
per1.get_balance()

    