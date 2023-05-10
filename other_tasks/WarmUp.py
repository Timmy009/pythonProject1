student_records = [{"id" : 1, "name" : "Timileyin", "score" :(90, 23, 45)}, {"id" : 2, "name" : "John", "score" :(56, 45, 21)},
                   {"id" : 3, "name" : "Esther", "score" :(87, 78, 54)}, {"id" : 4, "name" : "Victoria", "score" :(23, 56, 78)},
                   {"id" : 5, "name" : "Torin", "score" :(43, 32, 29)}
                   ]

student_records.append({"id" : 6, "name" : "Gbolahan", "score" :(87, 90, 40)})

student_records.append({"id" : 7, "name" : "Michael", "score" :(87, 98, 46)})

student_records.remove(student_records[3])

print(student_records)

for records in student_records:
    print(records)