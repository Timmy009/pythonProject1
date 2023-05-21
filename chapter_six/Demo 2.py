staff_dictionary = {
    1234: {
        "name": "John Doe",
        "date_of_birth": "1985-07-15",
        "office_branch": "New York"
    },
    5678: {
        "name": "Jane Smith",
        "date_of_birth": "1990-03-22",
        "office_branch": "London"
    },
    9012: {
        "name": "Michael Johnson",
        "date_of_birth": "1978-11-10",
        "office_branch": "Tokyo"
    }
}

# Display the dictionary's contents
for personnel_number, staff_info in staff_dictionary.items():
    print(f"Personnel Number: {personnel_number}")
    print("Staff Information:")
    print(f"  Name: {staff_info['name']}")
    print(f"  Date of Birth: {staff_info['date_of_birth']}")
    print(f"  Office Branch: {staff_info['office_branch']}")
    print()
