import random

def choose_operator(difficulty_level):
    if difficulty_level == 'easy':
        operators = ['+', '-']
    elif difficulty_level == 'medium':
        operators = ['+', '-', '*']
    elif difficulty_level == 'hard':
        operators = ['+', '-', '*', '/']
    else:
        print("Invalid difficulty level.")
        return None

    # Choose a random operator from the selected set
    return random.choice(operators)

def generate_random_equation(difficulty_level):
    if difficulty_level not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty level.")
        return None

    # Choose random numbers
    if difficulty_level == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif difficulty_level == 'medium':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    elif difficulty_level == 'hard':
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)

    # Choose random operator
    operator = choose_operator(difficulty_level)

    # Construct the equation
    equation = f"{num1} {operator} {num2}"

    return equation

# Example usage
difficulty = input("Choose difficulty level (easy, medium, hard): ").lower()
equation = generate_random_equation(difficulty)

if equation is not None:
    print("Random equation:", equation)