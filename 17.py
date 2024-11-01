import time
import pygame
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

def solve_equation():
    # Generate a random equation
    
    equation, answer = random_equation()
    print("Solve the equation:", equation)
    user_answer = float(input("Enter your answer: "))
    return user_answer == answer



def play_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("path_to_your_alarm_sound.mp3")  # Replace with the path to your alarm sound file
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up! Time to solve an equation!")
            while True:
                solved = solve_equation()
                if solved:
                    print("Congratulations! You solved the equation!")
                    break
                else:
                    print("Incorrect answer. Try again!")
        else:
            time.sleep(1)

        
         
def main():
    print("Enter the time for the alarm in HH:MM:SS format:")
    alarm_time = input()

    try:
        time.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
        return

    print(f"Alarm set for {alarm_time}")

    

    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
