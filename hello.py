x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
if x>=z and x>=y :
    l=x
elif y>=z and y>=x :
    l=y 
else:
    l=z
print(f"largest number is {l}")        