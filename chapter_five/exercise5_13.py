import string

key = "zyxwvutsrqponmlkjihgfedcba"

message = "Help me"

message =  message.lower()
message = "".join(char for char in message if char.isalpha())

encypted_message = " "

for char in message:
    position = string.ascii_lowercase.index(char)

    encyrpted_char = key[position]

    encypted_message += encyrpted_char

print(encypted_message)
