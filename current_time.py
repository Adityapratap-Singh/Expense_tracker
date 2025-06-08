from datetime import datetime

def get_current_time():
    """Returns the current time formatted as DD/MM/YYYY HH:MM:SS."""
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
