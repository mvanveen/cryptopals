import unittest

from main import (
    convert_hex_to_base64,
    fixed_xor,
)


class TestProblemSetOne(unittest.TestCase):
    def test_problem_one(self):
        hex_str = (
            '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        )

        self.assertEqual(
            convert_hex_to_base64(hex_str),
            'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        )

    def test_problem_one_fail_int(self):
        with self.assertRaises(TypeError):
            convert_hex_to_base64(42423)

    def test_problem_two(self):
        self.assertEqual(
            fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'),
            '746865206b696420646f6e277420706c6179'
        )

    def test_problem_two_fail_length(self):
        with self.assertRaises(ValueError):
            fixed_xor('1c', '686974207468652062756c6c277320657965')
