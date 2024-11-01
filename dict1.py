fruits = {"apples": "1.5kg", "mangoes": "2kg", "bananas": "1kg", "watermelon": "5kg"}
fruit_list = []  # Initialize an empty list to store fruits and their values

global_x = int(input("Enter the number of fruits: "))

while global_x > 0:
    fruit = input("Enter a fruit: ")
    
    if fruit in fruits:
        fruit_list.append((fruit, fruits[fruit]))  # Store a tuple (fruit, value)
        global_x -= 1
    else:
        print("Invalid fruit. Please enter a valid fruit.")

print("Selected fruits list:", fruit_list)
