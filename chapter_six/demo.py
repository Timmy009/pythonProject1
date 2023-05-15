def convert_number_to_words(number):
    # Define the dictionary mapping numbers to words
    num_words = {
        0: 'ZERO',
        1: 'ONE',
        2: 'TWO',
        3: 'THREE',
        4: 'FOUR',
        5: 'FIVE',
        6: 'SIX',
        7: 'SEVEN',
        8: 'EIGHT',
        9: 'NINE',
        10: 'TEN',
        11: 'ELEVEN',
        12: 'TWELVE',
        13: 'THIRTEEN',
        14: 'FOURTEEN',
        15: 'FIFTEEN',
        16: 'SIXTEEN',
        17: 'SEVENTEEN',
        18: 'EIGHTEEN',
        19: 'NINETEEN',
        20: 'TWENTY',
        30: 'THIRTY',
        40: 'FORTY',
        50: 'FIFTY',
        60: 'SIXTY',
        70: 'SEVENTY',
        80: 'EIGHTY',
        90: 'NINETY'
    }

    # Check if the number is already defined in the dictionary
    if number in num_words:
        return num_words[number]

    # Convert the number to words
    words = []
    if number >= 100:
        hundreds = number // 100
        words.append(num_words[hundreds] + ' HUNDRED')
        number %= 100

    if number >= 20:
        tens = (number // 10) * 10
        words.append(num_words[tens])
        number %= 10

    if number > 0:
        words.append(num_words[number])

    return ' '.join(words)


def convert_amount_to_words(amount):
    dollars, cents = str(amount).split('.')
    dollars = int(dollars)
    cents = int(cents)

    # Convert dollars to words
    if dollars == 0:
        dollars_words = 'ZERO'
    else:
        dollars_words = convert_number_to_words(dollars)

    # Convert cents to words
    if cents == 0:
        cents_words = 'ZERO'
    else:
        cents_words = convert_number_to_words(cents)

    # Construct the final word equivalent
    if dollars == 1:
        dollars_label = 'DOLLAR'
    else:
        dollars_label = 'DOLLARS'

    if cents == 1:
        cents_label = 'CENT'
    else:
        cents_label = 'CENTS'

    result = dollars_words + ' ' + dollars_label + ' AND ' + cents_words + ' ' + cents_label
    return result


# Prompt the user for the numeric check amount
amount = float(input("Enter the check amount (less than 1000): "))

# Convert the amount to words
words = convert_amount_to_words(amount)

# Print the word equivalent of the amount
print("Amount in words:", words)
