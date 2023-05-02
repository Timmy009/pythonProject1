import itertools


def password_generator(password):
    text = itertools.permutations(password)
    perm = []
    for text in text:
        perm += text
    return perm

print(password_generator("we1"))
