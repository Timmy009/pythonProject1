import random

# Generate a list of 8000 user IDs
user_ids = []
for i in range(8000):
    letter = random.choice(['a', 'b', 'c', 'd', 'e', 'f'])
    number1 = random.randint(1, 4)
    number2 = random.randint(1, 4)
    user_id = letter + str(number1) + str(number2)
    user_ids.append(user_id)

# Remove duplicates and sort in descending order
unique_sorted_user_ids = sorted(set(user_ids), reverse=True)

# Print the sorted user IDs
print(unique_sorted_user_ids)
