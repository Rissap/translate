from enum import Enum


class NumberType(Enum):
    ROMAN = 'ROMAN'
    ARABIC = 'ARABIC'


roman_numbers = ['M', 'D', 'C', 'L', 'X', 'V', 'I']


roman_arabic_equivalent = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
