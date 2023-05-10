from collections import deque

list1 = deque([])

list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)


print(list1)

list1.popleft()
list1.popleft()
list1.popleft()
print(list1)