import statistics


def changing(sample: str):
    sample = list(sample)
    new_str = ""
    max1 = statistics.mode(sample)

    for index, l in enumerate(sample):
        if l == max1 and index > 1:
            l = "$"
            new_str = new_str + l
        else:
            new_str = new_str + l

    return new_str


print(changing("restart"))
print(changing("simi"))

print(changing("deep"))
