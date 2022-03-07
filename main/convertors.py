from main.models import History

import datetime as dt
from main.constants import NumberType, roman_numbers, roman_arabic_equivalent


def save_history(raw, num):
    """
    save latest 6 conversion
    revrite the oldest one
    """
    if History.objects.all().count() > 6:
        tmp = History.objects.latest()
    else:
        tmp = History()

    tmp.from_num = raw
    tmp.to_num = num
    tmp.time = dt.datetime.now()
    tmp.save()


def get_number_type(raw_number: str):
    """
    Check, if number is arabic or roman.
    Raise value error if number is not roman nor arabic
    """

    if raw_number.isdigit():
        return NumberType.ARABIC

    if set(raw_number).issubset(set(roman_numbers)):
        return NumberType.ROMAN

    raise ValueError('Number is not roman nor arabic.')


def convert_to_roman(number: int) -> str:
    """
    Convert integer from arabic to roman
    """
    roman_number = ""

    for index, numeral in enumerate(roman_numbers):
        numeral_amount = number // roman_arabic_equivalent[numeral]

        if numeral_amount > 3 and numeral != 'M':
            previous_numeral = roman_numbers[index - 1]
            roman_number += numeral + previous_numeral
            number -= (
                roman_arabic_equivalent[numeral] 
                + roman_arabic_equivalent[previous_numeral]
            )

        else:
            roman_number += numeral * numeral_amount
            number -= roman_arabic_equivalent[numeral] * numeral_amount

    return roman_number


def convert_to_arabic(number: str) -> int:
    """
    Convert roman number to arabic
    """

    num = list(number.upper())
    calc = []
    res = 0

    # convert roman to arabic
    for x in num:
        calc.append(int(roman_arabic_equivalent[x]))

    # calculate with the rules of roman number position
    for x in range(len(calc) - 1):
        if calc[x] < calc[x + 1]:
            calc[x] = calc[x] * (-1)

    return sum(calc)
