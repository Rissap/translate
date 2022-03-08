from difflib import get_close_matches
from main.models import History

import datetime as dt
from main.constants import (
    NumberType, 
    roman_numbers, 
    roman_arabic_equivalent,
    prioroty_combinations,
)


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


def get_closest_roman(number):
    for roman in roman_numbers:
        if roman_arabic_equivalent[roman] <= number:
            return roman, roman_arabic_equivalent[roman]


def convert_to_roman(number: int) -> str:
    """
    Convert integer from arabic to roman
    """
    roman_number = ""

    while number > 0:
        roman, value = get_closest_roman(number)
        roman_amount = number // value
        roman_number += roman * roman_amount
        number -= value * roman_amount

    return roman_number


def convert_to_arabic(number: str) -> int:
    """
    Convert roman number to arabic
    """

    arabic = 0
    number = number.upper()

    for numerals in [prioroty_combinations, roman_numbers]:
        for numeral in numerals:
            numeral_amount = len(number.split(numeral)) - 1
            arabic += roman_arabic_equivalent[numeral] * numeral_amount
            number = ''.join(number.split(numeral))

    return arabic
