import unittest
from src.utils.validators import BrazilianPhoneValidator

class TestPhoneValidator(unittest.TestCase):

    def test_isBrazilianPhoneNumber(self):
        

        valid = [
        "83 92646 2141",
        "83 0800 2141"
        ]

        invalid= [
        "55 83 92646 2141",
        "(83) 92646-2141",
        "(83) 92646 2141",
        "83 92646-2141",
        "83 62646 2141",
        "83 9646 2141",
        "8326462141",
        "83 26462141",
        "832646 2141",
        "83 26462 141"
        ]


        for phone in valid:
            phoneValidator = BrazilianPhoneValidator(phone)
            self.assertEqual(phoneValidator.isBrazilianPhoneNumber(), True)

        for phone in invalid:
            phoneValidator = BrazilianPhoneValidator(phone)
            self.assertEqual(phoneValidator.isBrazilianPhoneNumber(), False)