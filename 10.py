def main():
    meow(number)
    number=get_number()

        
def get_number():
    while True:
        n=int(input("what's n"))
        if n>0:
            break
    return n        

    

def meow(n):
    for i in range(n):
        print("meow")
