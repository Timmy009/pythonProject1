def converter(dollar: int) -> str:
    conversion_rate = 750
    naira = conversion_rate * dollar
    return f"The naira amount of {dollar} dollars is {naira: ,.2f}"


dollar = int(input("Tell me the dollar amount to convert: "))
print(converter(dollar))
