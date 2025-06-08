def clear_file(filename):
    """Clear all expense entries from the file."""
    try:
        with open(filename, 'w', encoding='utf-8'):
            pass
        return True
    except Exception as e:
        print(f"Error clearing file: {e}")
        return False