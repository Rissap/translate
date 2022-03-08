from enum import Enum


class NumberType(Enum):
    ROMAN = 'ROMAN'
    ARABIC = 'ARABIC'

roman_arabic_equivalent = {
    'M': 1000,       
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}

roman_numbers = list(roman_arabic_equivalent.keys())

prioroty_combinations = list(filter(lambda x: len(x) == 2, roman_numbers))
