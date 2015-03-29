import unittest

from main import convert_hex_to_base64


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
