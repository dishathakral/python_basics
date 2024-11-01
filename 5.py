a = input("Enter first number: ")
b = input("Enter second number: ")

# Check if inputs are convertible to integers
try:
    a = int(a)
    b = int(b)
    z = a + b
    print(z)
except ValueError:
    print("Please enter valid integers.")
