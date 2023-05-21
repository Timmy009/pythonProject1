def register():
    name_register = {"esther": 23, "timi": 26, "mariam": 34}
    name = input("Enter your name: ").lower()
    if name in name_register:
        return f"Hi,  {name}.  You are   {name_register[name]}  years old"
    else:
        print("Your age is not on the register: ")
        print("Enter your age to register on the database: ")
        age = input()
        name_register[name] = age
        return f"Hi, {name}, You are {name_register[name]} years old"


print(register())
