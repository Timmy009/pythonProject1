def pallindrome(name):
    reverse_name = name[::-1]
    if reverse_name == name:
        return f"{name} is a pallundrome"
    else:
        return f"{name} is not a pallundrome"

print(pallindrome("madam"))

print(pallindrome("timi"))