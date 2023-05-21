def get_largest_element(list2):
    largest_element = list2[0]
    for element in list2:
        if len(element) > len(largest_element):
            largest_element = element
    return largest_element, len(largest_element)


list2 = ["esther", "sultan", "emmanuel"]
print(get_largest_element(list2))
