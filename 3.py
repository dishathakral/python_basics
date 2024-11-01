#ask user there nameprint("what's your name")
a=input("what's your name ").strip().upper()
first, last=a.split(" ")
print(f"hello, {first}")
