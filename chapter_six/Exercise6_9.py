tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

print("(a) Show the abbreviation of a country chosen by the user.")
print("(b)Display all key-value pairs in a two-column format.")
print("(c)Add a new key-value pair to the dictionary or change the value of an existing key-value pair.")
print("(d) Create a new dictionary with the values of the first dictionary as keys and the keys of the first dictionary as values.")
print("e) Convert all the abbreviations in the dictionary to uppercase letters.")

options = input()

if options.lower() == "a":
    print("Enter a country to get the abbrevaition")
    country = input()
    if country in tlds:
        abb = tlds[country]
        print(abb)
    else:
        print("Invalid Input. Country not found")
if options.lower() == "b":
    for country, abs in tlds.items():
        print(country, abs)
        print()


if options.lower() == "c":
    added_country = input("Enter country to be added: ")
    abbreviation  = input("Enter the abbreviated value: ")
    tlds[added_country] = abbreviation
    print("Country added successfully: ")
    print(tlds)

if options.lower() == "d":
    reversed = {abbreviation : country for country, abbreviation in tlds.items()}
    print(reversed)



if options.lower() == "e":
    upper = {abbreviation.upper() : country.upper() for abbreviation, country in tlds.items()}
    print(upper)


