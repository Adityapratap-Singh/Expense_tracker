from write import write_to_file
from read import read_from_file

FILENAME = "exp.txt"


def add_expense():
    """Prompt user to add an expense and write to file."""
    description = input("Enter expense description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return
    while True:
        amount_str = input("Enter amount (e.g. 12.50): ").strip()
        try:
            amount = float(amount_str)
            if amount < 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number like 10.99.")
    success = write_to_file(FILENAME, description, amount)
    if success:
        print("Expense added successfully.\n")
    else:
        print("Failed to add expense.\n")