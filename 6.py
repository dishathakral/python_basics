try:
    # Code that may raise an exception
    x = int("abc")  # This will raise a ValueError
except ValueError as e:
    # Code to handle the exception
    print(f"Error: {e}")
