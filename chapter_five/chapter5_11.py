import string


def encrypt (message):
    message = message.replace(" ", "")
    message.replace(",", "")
    message = message.casefold()
    unicode_code = set(message)
    if unicode_code.issubset(string.ascii_letters):
        return unicode_code
    else:
        return string.ascii_letters

print(encrypt("my name is timi"))


print(string.ascii_letters)

