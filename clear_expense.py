# clear_expense.py
from clear import clear_file
FILENAME = "exp.txt"

def clear_expenses(filename):
    """Confirm and clear all expenses."""
    confirm = input("Are you sure you want to clear all expenses? Type YES to confirm: ").strip()
    if confirm == "YES" or confirm == "yes" or confirm == "Yes" or confirm == "y" or confirm == "Y":
        success = clear_file(FILENAME)
        if success:
            print("All expenses cleared.\n")
        else:
            print("Failed to clear expenses.\n")
    else:
        print("Clear cancelled.\n")