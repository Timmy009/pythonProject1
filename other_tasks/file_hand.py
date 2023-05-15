# file = open("student_records.txt", mode="w")
# file.write("001 mariam 75 \n")
# file.write("002 david 75 \n")
# file.write("004 torin 75 \n")
#
# file.close()
#
# with open("record2.txt", mode="a") as file:
#     file.write("001 semicolon \n")
#
# file1 = open("record2.txt", mode="r")
#
# file2 = open("record.txt", mode="w")
#
# with file1, file2:
#     for record in file1:
#         sn, name, score = record.split()
#         if sn != "008":
#             file2.write(record)
#         else:
#             new_record = " ".join([sn, "oluwadurotimi", score])
#             file2.write(new_record + "\n")


import json

records = {"student_records": [
    {"id": 1, "name": "ebuka", "age": 41},
    {"id": 2, "name": "dele", "age": 44},
    {"id": 3, "name": "sultan", "age": 31},
]}

with open ("records.json", mode="w") as rec:
    json.dump(records, rec)

with open ("records.json", mode="r") as rec2:
    print(json.dumps(json.load(rec2), indent=4))