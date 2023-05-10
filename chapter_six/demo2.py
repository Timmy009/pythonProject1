# Dictionary mapping numbers to their word equivalents
NUMBERS_TO_WORDS = {
    0: "ZERO",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE",
    10: "TEN",
    11: "ELEVEN",
    12: "TWELVE",
    13: "THIRTEEN",
    14: "FOURTEEN",
    15: "FIFTEEN",
    16: "SIXTEEN",
    17: "SEVENTEEN",
    18: "EIGHTEEN",
    19: "NINETEEN",
    20: "TWENTY",
    30: "THIRTY",
    40: "FORTY",
    50: "FIFTY",
    60: "SIXTY",
    70: "SEVENTY",
    80: "EIGHTY",
    90: "NINETY",
}

def number_to_words(num):
    if num == 0:
        return "ZERO"
    elif num < 0 or num >= 1000:
        return "INVALID AMOUNT"
    else:
        words = ""
        # Convert hundreds digit
        if num >= 100:
            words += NUMBERS_TO_WORDS[num // 100] + " HUNDRED "
            num %= 100
        # Convert tens digit and units digit
        if num > 0:
            if num < 20:
                words += NUMBERS_TO_WORDS[num]
            else:
                words += NUMBERS_TO_WORDS[(num // 10) * 10] + " "
                num %= 10
            if num > 0:
                words += "AND " + NUMBERS_TO_WORDS[num]
        return words

# Input check amount
check_amount = float(input("Enter check amount: "))
check_dollars = int(check_amount)
check_cents = int((check_amount - check_dollars) * 100)

# Convert dollars to words
dollars_words = number_to_words(check_dollars)

# Convert cents to words
cents_words = f"{check_cents:02d}/100"

# Print check amount in words
print(f"{dollars_words} AND {cents_words}")
