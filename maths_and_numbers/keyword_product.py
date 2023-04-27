def multiple (*lst):
    product = 1
    for num in lst:
        product *= num
    return product


print(multiple(4, 2, 7))



def get_user (**user):
    print(user)
    print(user["fname"])


get_user(id=1, fname="michael", lname= "friday")