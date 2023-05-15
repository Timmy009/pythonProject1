tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

def show_abbreviation():
    country = input("Enter a country name: ")
    if country in tlds:
        abbreviation = tlds[country]
        print(f"The abbreviation of {country} is {abbreviation}")
    else:
        print("Country not found in the dictionary.")

def display_key_value_pairs():
    print("Key\t\tValue")
    print("------------------")
    for country, abbreviation in tlds.items():
        print(f"{country}\t\t{abbreviation}")

def add_or_update_pair():
    country = input("Enter a country name: ")
    abbreviation = input("Enter the abbreviation: ")
    tlds[country] = abbreviation
    print("Key-value pair added/updated successfully.")

def create_reverse_dictionary():
    reverse_tlds = {abbreviation: country for country, abbreviation in tlds.items()}
    print("Reverse dictionary created successfully:")
    print(reverse_tlds)

def convert_abbreviations_to_uppercase():
    uppercase_tlds = {country: abbreviation.upper() for country, abbreviation in tlds.items()}
    print("Abbreviations converted to uppercase successfully:")
    print(uppercase_tlds)

# Prompt the user for the manipulation option
while True:
    print("\nDictionary Manipulation Options:")
    print("a) Show the abbreviation of a country")
    print("b) Display all key-value pairs")
    print("c) Add/change a key-value pair")
    print("d) Create a reverse dictionary")
    print("e) Convert abbreviations to uppercase")
    print("q) Quit the program")

    choice = input("Enter your choice: ")
    print("------------------")

    if choice == 'a':
        show_abbreviation()
    elif choice == 'b':
        display_key_value_pairs()
    elif choice == 'c':
        add_or_update_pair()
    elif choice == 'd':
        create_reverse_dictionary()
    elif choice == 'e':
        convert_abbreviations_to_uppercase()
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please try again.")
