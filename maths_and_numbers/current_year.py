import datetime


def calculate_age(year_of_birth: int) -> str:
    today = datetime.date.today()
    current_year = today.year
    age = current_year - year_of_birth
    return f"Your age is {age}"


year_of_birth = int(input("What is your year of birth? "))
print(calculate_age(year_of_birth))
