stack = []
print(stack)
stack.append("timmy")
print(stack)
stack.append("Tayo")
print(stack)
stack.pop()
print(stack)

letters = ("a", "b", "c")
print(letters)
print(type(letters))

number = (1,)
print(type(number))

num = 1, 2, 3

print(type(num))

alpha_num = letters + num

print(alpha_num)

print(alpha_num[1:3])

nam = tuple(range(1, 501))
print(nam)

nam_odd = tuple(range(2, 501, 2))
print(nam_odd)

nam_even = nam = tuple(range(1, 501, 2))

print(nam_even)

nam_both = nam_even + nam_odd

print(nam_both)
nume = 1, 2, 3

print(type(nume))
num = 1, 2, 3, 4, 5

i, j, *other = num

print(i)
print(other)
me = 1, 2, 3, 4, 5,
x, *others, y = me
print(others)
print(y)