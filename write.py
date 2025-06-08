from current_time import *


def write_to_file(filename, description, amount):
    """Append an expense entry to the file."""
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            timestamp = get_current_time()
            file.write(f"{timestamp} - {description} - {amount:.2f}\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False