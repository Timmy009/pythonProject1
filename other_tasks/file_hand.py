file = open("student_records.txt", mode="w")
file.write("001 mariam 75 \n")
file.write("002 david 75 \n")
file.write("003 timi 75 \n")
file.write("004 torin 75 \n")

file.close()

with open("record2.txt", mode="w") as file:
    file.write("001 mariam 75 \n")
    file.write("002 david 75 \n")
    file.write("003 timi 75 \n")
    file.write("004 torin 75 \n")