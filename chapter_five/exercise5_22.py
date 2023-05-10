from collections import deque

list2 = deque([])

list2.append(1)
list2.append(2)
list2.append(3)

print(list2)

list2.popleft()
list2.popleft()

print(list2)