with open("record2.txt", mode='r') as records:
    for record in records:
        num, name, score = record.split()
        print(f"{num: <10} {name: <10} {score: >10}")