name=input("enter the name:")
match name:
    case "harry" | "ron" | "hermione":
        print("gryffindor")
    case "draco":
        print("slytherin")
    case _:  
        print("who?")      
