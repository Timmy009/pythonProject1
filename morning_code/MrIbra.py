def max1(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max


def mix1(arr):
    max = arr[0]
    for i in arr:
        if i < max:
            max = i
    return max


def sum1(arr):
    total = 0
    for i in arr:
        total = total + i
    return total


def arrange(arr):
    index1 = 0
    while index1 < len(arr):
        index = index1 + 1
        while index < len(arr):
            if arr[index1] > arr[index]:
                arr[index1], arr[index] = arr[index], arr[index1]
            index = index + 1
        index1 = index1 + 1

    return arr


def de_arrange(arr):
    index1 = 0
    while index1 < len(arr):
        index = index1 + 1
        while index < len(arr):
            if arr[index1] < arr[index]:
                arr[index1], arr[index] = arr[index], arr[index1]
            index = index + 1
        index1 = index1 + 1

    return arr


arr = [2, 9, 3, 1]
print(max1(arr))
print(mix1(arr))
print(sum1(arr))
print(arrange(arr))
print(de_arrange(arr))
