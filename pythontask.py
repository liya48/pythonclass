import datetime
from tabulate import tabulate

class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self):
        return f"{self.amount} {self.category} {self.date}"

def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    expense = Expense(amount, category, date)
    expenses.append(expense)

def view_expenses(expenses):
    table = [[expense.amount, expense.category, expense.date] for expense in expenses]
    headers = ["Amount", "Category", "Date"]
    print(tabulate(table, headers=headers, tablefmt="grid"))

def search_expenses(expenses):
    print("Search by:")
    print("1. Category")
    print("2. Date")
    choice = input("Enter your choice: ")
    if choice == "1":
        category = input("Enter category: ")
        results = [expense for expense in expenses if expense.category == category]
    elif choice == "2":
        date = input("Enter date (YYYY-MM-DD): ")
        results = [expense for expense in expenses if expense.date == date]
    else:
        print("Invalid choice.")
        return
    if results:
        table = [[expense.amount, expense.category, expense.date] for expense in results]
        headers = ["Amount", "Category", "Date"]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    else:
        print("No expenses found.")

def total_spent(expenses):
    total = sum(expense.amount for expense in expenses)
    print(f"Total spent: {total}")

def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense.amount},{expense.category},{expense.date}\n")

def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = []
            for line in file.readlines():
                amount, category, date = line.strip().split(",")
                expenses.append(Expense(float(amount), category, date))
            return expenses
    except FileNotFoundError:
        return []

def main():
    expenses = load_expenses()
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses")
        print("4. Show Total Spent")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            search_expenses(expenses)
        elif choice == "4":
            total_spent(expenses)
        elif choice == "5":
            save_expenses(expenses)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__== "__main__":
    main()