fruits={"apples":"1.5kg",
        "mangoes":"2kg",
        "bananas":"1kg",
        "watermelon":"5kg"}
fruit_list=[]#initializing empty list.
global_x=int(input("first tell the number of fruits:"))
while global_x>0:
    fruit=input("what fruit ")
    
    if fruit in fruits:
        fruit_list.append((fruit , fruits[fruit]))
        global_x=global_x-1
    else:
        print("valid name")

print(fruit_list)


