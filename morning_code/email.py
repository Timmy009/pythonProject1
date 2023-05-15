def username_generator(email):
    username = ""
    for name in email:
        if name != "@":
            username += name
        else:
            break
    return username


def username_generator2(email:str):
    username = email.split("@")[0]
    return f"Your username is {username}"



email = input("enter your mail: ")



print(username_generator2(email))
print("Your username is ", username_generator(email))
