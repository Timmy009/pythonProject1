name = input("Enter name: ")
name = name.title().lower()
b = name[::-1]

if b == name:
    print("This is a pallindrome")
else :
    print ("This is not a pallindrome")