from multiprocessing.sharedctypes import Value
from tokenize import Number
from django.test import TestCase

from main.constants import NumberType, roman_arabic_equivalent
from main.convertors import (
    convert_to_arabic,
    convert_to_roman,
    get_number_type,
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
            'McDIX': 1409,
        }
        self.number_type_cases = {
            '1': NumberType.ARABIC,
            '999': NumberType.ARABIC,
            '-1': ValueError,
            'I': NumberType.ROMAN,
            'IX': NumberType.ROMAN,
            'MMCCLLXXIII': NumberType.ROMAN,
            'MLOPQ': ValueError,
            'random': ValueError,
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

    def test_number_type(self):
        for number, expected_value in self.number_type_cases.items():
            with self.subTest(f'{number=} {expected_value=}'):
                if type(expected_value) == Exception:
                    with self.assertRaises(ValueError):
                        get_number_type(number)
                else:
                    self.assertEqual(get_number_type(number), expected_value)
