def read_from_file(filename):
    """Read all expense entries from the file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]
        return lines
    except Exception as e:
        print(f"Error reading file: {e}")
        return []