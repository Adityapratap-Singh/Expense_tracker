from current_time import *

def filter_expenses(expenses):
    """Filter expenses by date and print them."""
    selected_date = input("Enter date to filter expenses (DD/MM/YYYY): ").strip()
    try:
        selected_date = datetime.strptime(selected_date, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY.")
        return

    print(f"\nExpenses for {selected_date.strftime('%d/%m/%Y')}:\n" + "-"*50)
    total = 0.0
    found = False
    for line in expenses:
        try:
            timestamp, description, amount_str = line.split(" - ")
            timestamp_date = datetime.strptime(timestamp, "%d/%m/%Y %H:%M:%S").date()
            if timestamp_date == selected_date:
                amount = float(amount_str)
                total += amount
                print(f"[{timestamp}] {description} : ${amount:.2f}")
                found = True
        except ValueError:
            print(line)
    if not found:
        print("No expenses found for this date.")
    print("-"*50)
    print(f"Total spent on {selected_date.strftime('%d/%m/%Y')}: ${total:.2f}\n")