def main():
    a=int(input("enter the number:"))
    if if_even(a):
        print("even")
    else:
        print("odd")


def if_even(n):
    return  n%2==0

main()    