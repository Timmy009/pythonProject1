def sort_list(text):
    for num in range(len(text)):
        for num2 in range(num+1  ,len(text)):
            if text[num] > text[num2]:
                text[num], text[num2] = text[num2], text[num]
    return text

lst = [25, 10, 15, 5, 30, 55, 35, 45, 20]

print(sort_list(lst))

print(sorted(lst))



if sort_list(lst) == sorted(lst):
    print("true")




