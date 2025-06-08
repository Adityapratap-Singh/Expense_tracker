def show_expenses(expenses):
    """Nicely print the list of expenses."""
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return
    print("\nYour expenses:\n" + "-"*50)
    total = 0.0
    for line in expenses:
        try:
            timestamp, description, amount_str = line.split(" - ")
            amount = float(amount_str)
            total += amount
            print(f"[{timestamp}] {description} : ${amount:.2f}")
        except ValueError:
            # Malformed line, just print raw
            print(line)
    print("-"*50)
    print(f"Total spent: ${total:.2f}\n")