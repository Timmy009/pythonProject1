names = [("Timileyin", "Bamgbose"), ("John", "Jones"), ("Elizabeth", "Hok"), ("Mat", "Jones"), ("Ella", "Mark"),
         ("Dan", "Lok"), ("Brain", "Jones")]

jones_finds = list(filter(lambda x: x[1] == "Jones", names))

for name in jones_finds:
    print(name)
