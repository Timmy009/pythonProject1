votes = 'john,jane,john,john,bob,jane,john,jane'

candidates = {}

for name in votes.split(","):
    if name in candidates:
        candidates[name] +=1
    else:
        candidates[name] = 1


for count1, name in candidates.items():
    print(f"{count1}: {name}")