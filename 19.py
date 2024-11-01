import datetime
import time
import random

current= datetime.datetime.now()
print(current)

def generate_random_equation():
    # Generate two random integers between 1 and 10
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    # Generate a random operator
    operator = random.choice(['+', '-', '*', '/'])
    # Construct the equation string
    equation = f"{a} {operator} {b}"
    # Calculate the correct answer
    if operator == '+':
        answer = a + b
    elif operator == '-':
        answer = a - b
    elif operator == '*':
        answer = a * b
    else:
        answer = a / b
    return equation, answer

def solve_equation():
    # Generate a random equation
    equation, answer = generate_random_equation()
    print("Solve the equation:", equation)
    user_answer = float(input("Enter your answer: "))
    return user_answer == answer

def set_alarm(hour, minute):
    current_time = datetime.datetime.now()
    alarm_time = current_time.replace(hour=hour, minute=minute, second=0, microsecond=0)
    print("Alarm set for:", alarm_time.strftime("%H:%M"))

    time_difference = (alarm_time - current_time).total_seconds()
    time.sleep(time_difference)

    while True:
        print("Wake up! Time to solve an equation!")
        solved = solve_equation()
        if solved:
            print("Congratulations! You solved the equation!")
            break
        else:
            print("Incorrect answer. Try again!")

if _name_ == "_main_":
    # Set the alarm time (hour and minute)
    alarm_hour = int(input("Enter the hour for the alarm (0-23): "))
    alarm_minute = int(input("Enter the minute for the alarm (0-59): "))

    # Call the set_alarm function
    set_alarm(alarm_hour, alarm_minute)