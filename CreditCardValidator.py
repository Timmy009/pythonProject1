class CreditCardValidator:
    def __init__(self, credit_card_number):
        # self.validate_input(credit_card_number)
        self.validate_length(credit_card_number)
        self.credit_card_number = credit_card_number

    # def validate_input(self, credit_card_number: str):
    #     if credit_card_number.__contains__("0-9"):
    #         return "Valid"
    #     # else:
    #     #     raise ValueError

    def validate_length(self, credit_card_number):
        if len(credit_card_number) >= 13 or len(credit_card_number) >= 16:
            return "Valid"
        else:
            return "Invalid"

    def validate_card_type(self, credit_card_number: str):
        if self.validate_length(credit_card_number) == "Valid":
            if credit_card_number.startswith("4"):
                return "Visa Cards"
            elif credit_card_number.startswith("5"):
                return "MasterCard"
            elif credit_card_number[0:2] == "37":
                return "American Express Card"
            elif credit_card_number.startswith("6"):
                return "Discover Cards"
        else:
            "The lenght is Invalid"

    def doublingEverySecondDigit(self, creditCardNumber: str):
        sum = 0
        innerInt = 0
        count = len(creditCardNumber) - 2
        while count >= 0:
            digit = int(creditCardNumber[count])
            numberDigit = int(digit)
            doubleNumber = numberDigit + numberDigit
            if doubleNumber > 9:
                doubleString = str(doubleNumber)
                index = len(doubleString) - 1
                while index >= 0:
                    doubleNumber = innerInt
                    valString = str(doubleString[index])
                    innerInt = int(valString)
                    doubleNumber += innerInt
                    index -= 1
            count -= 2
            sum += doubleNumber
        return sum

    def add_single_digit_in_odd_places(self, credit_card_number):
        sum = 0
        for number in credit_card_number[::-2]:
            sum += int(number)
        return sum

    def sum_result(self, credit_card_number):
        return self.doublingEverySecondDigit(credit_card_number) + self.add_single_digit_in_odd_places(
            credit_card_number)

    def validate(self, credit_card_number) -> str:
        if self.sum_result(credit_card_number) % 10 == 0:
            return "Valid"
        else:
            return "Invalid"


card = input("Hi, Kindly enter your card details: ")
card_one = CreditCardValidator(card)
print(f"The card type is {card_one.validate_card_type(card)}")
print(f"The length of the card is {len(card)}. so this card length is {card_one.validate_length(card)}")
print(f"The card number is {card}")
print(f"The validatity status of this card is {card_one.validate(card)}")
