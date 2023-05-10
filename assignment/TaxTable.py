def compute_tax(status, taxable_income):
    status = status.lower()
    tax = 0
    match status:
        case "single":
            tax = taxable_income * 0.17376
        case "married joint":
            tax = taxable_income * 0.1333
        case "married seperate":
            tax = taxable_income * 0.17376
        case "Head of a house":
           tax =  taxable_income * 0.14704
    return tax

status = input("Enter your status: ")
taxable_income = int(input("Enter your taxable income: "))

print( "Your tax is ",compute_tax(status, taxable_income))
