FILENAME = "exp.txt"
from current_time import *
from write import *
from read import *
from clear import *
from show_expense import *
from filter_expense import *
from add_expense import *
from clear_expense import *

filename = "exp.txt"

class ExpenseTracker:
    def __init__(self, filename):
        self.filename = filename

    def main_menu(self):
        print("== Expense Tracker ==")
        print("1. View expenses")
        print("2. Add expense")
        print("3. Clear all expenses")
        print("4. Filter expenses by date")
        print("5. Exit")
        choice = input("Select an option (1-5): ").strip()
        return choice

    def run(self):
        while True:
            choice = self.main_menu()
            if choice == '1':
                expenses = read_from_file(self.filename)
                show_expenses(expenses)
            elif choice == '2':
                add_expense(self.filename)
            elif choice == '3':
                clear_expenses(self.filename)
            elif choice == '4':
                expenses = read_from_file(self.filename)
                if expenses:
                    print("Filtering expenses by date...")
                    filter_expenses(expenses)
                else:
                    print("No expenses to filter.\n")
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.\n")

if __name__ == "__main__":
    tracker = ExpenseTracker(FILENAME)
    tracker.run()