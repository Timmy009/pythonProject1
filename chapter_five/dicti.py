days_per_month = {'January': 31, 'February': 28, 'March': 31}

days_per_month["April"] = 45
days_per_month.pop("January")
the_view = days_per_month.values()

ke =  list(days_per_month.keys())
print(sorted(ke))

for value in the_view:
    days_per_month['February'] = "dec"
    print(f" {value}")


days_per_month.get("January")

