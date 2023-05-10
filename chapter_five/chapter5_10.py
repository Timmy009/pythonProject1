import itertools


def password_generator(password):
    letters = password[:2]
    digits = password[2]
    text = itertools.permutations(letters+digits, len(password))
    perm = []
    for text in text:
        perm.append(text)
    return perm

print(password_generator("we1"))
