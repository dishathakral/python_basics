import random

def op(level):
    if level == 'easy':
        operator = ['+', '-']
    elif level == 'medium':
        operator = ['+', '-', '*']
    elif level == 'hard':
        operator = ['+', '-', '*', '/']
    else:
        
        print("Invalid difficulty level.")
        return None
    

    # Choose a random operator from the selected set
    return random.choice(operator)

def random_equation(level):
    if level not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty level.")
        return None

    # Choose random numbers
    if level == 'easy':
        num1 = random.randint(1, 10)# Choose random operator
        num2 = random.randint(1, 10)
        operator = op(level)
        equation = f"{num1} {operator} {num2}"# Construct the equation
    elif level == 'medium':
        num1 = random.randint(1, 100)# Choose random operator
        num2 = random.randint(1, 100)
        num3 = random.randint(1,10)
        operator1 = op(level)
        operator2 = op(level)
        equation = f"{num1} {operator1} {num2} {operator2}{num3}"# Construct the equation
    elif level == 'hard':
        num1 = random.randint(1, 1000)# Choose random operator
        num2 = random.randint(1, 1000)
        num3 = random.randint(1,100)
        num4= random.randint(1,10)
        operator1 = op(level)
        operator2 = op(level)
        operator3 = op(level)
        equation = f"{num1} {operator1} {num2} {operator2}{num3}{operator3}{num4}"# Construct the equation
    return equation

# Example usage
difficulty = input("Choose difficulty level (easy, medium, hard): ").lower()
equation = random_equation(difficulty)

if equation is not None:
    print("Random equation:", equation)