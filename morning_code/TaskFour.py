def find(letter: str):
    low_case = []
    for ind, n in enumerate(letter):
        if n == n.lower():
            low_case.append(ind)
    return low_case


letter = "EsTheR"
print(find(letter))

t = range(5)

print(t)
print(type((1,)))