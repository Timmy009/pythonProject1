passes = 0  # number of passes
failures = 0  # number of failures
# process 10 students
count = 1
while count <= 10:
    result = int(input('Enter result (1=pass, 2=fail): '))
    if result == 1 or result == 2:
        count +=1
        if result == 1:
            passes = passes + 1

failures = 10 - passes
print('Passed:', passes)
print('Failed:', failures)
if passes > 8:
    print('Bonus to instructor')
