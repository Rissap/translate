from django.test import TestCase

from main.convertors import (
    convert_to_roman,
    convert_to_arabic,
    get_number_type,
)
from main.constants import (
    NumberType, roman_numbers, roman_arabic_equivalent,
)


class ConvertorsTestCase(TestCase):
    def setUp(self):
        self.numbers_cases = {
            'XII': 12,
            'xvi': 16,
            'Xiv': 14,
            'MXV': 1015,
            'MLXIV': 1064,
            'MDIV': 1504,
            'MCDIX': 1409,
        }

    def test_single_number_convert(self):
        for roman, arabic in roman_arabic_equivalent.items():
            with self.subTest(f'{roman=} {arabic=}'):
                converted_arabic = convert_to_arabic(roman)
                converted_roman = convert_to_roman(arabic)
                self.assertEqual(arabic, converted_arabic)
                self.assertEqual(roman, converted_roman)

    def test_complex_numbers_convert(self):
        for roman, arabic in self.numbers_cases.items():
            converted_arabic = convert_to_arabic(roman)
            converted_roman = convert_to_roman(arabic)
            self.assertEqual(arabic, converted_arabic)
            self.assertEqual(roman.upper(), converted_roman)
