import unittest
from src.utils.validators import BrazilianPhoneValidator

class TestPhoneValidator(unittest.TestCase):
    def setUp(self):

        self.validCellPhoneNumbers = [
            "81 98765 4321",
            "83 92646 2141",
            "11 91111 1111"
        ]

        self.validLandlinePhoneNumbers = [
            "81 8765 4321",
            "83 0800 2141",
            "11 1111 1111"
        ]
        
        self.invalidCellPhoneNumbers = [
            "83 18765 4321",
            "(83) 98765 4321",
            "55 83 98765 4321",
            "+55 (83) 98765 4321",
            "83987654321",
            "83 987654321",
            "8398765 4321",
            "aa aaaaa aaaa",
            " ",
            ""
        ]

        self.invalidLandlinePhoneNumbers = [
            "83 9765 4321",
            "(83) 8765 4321",
            "55 83 8765 4321",
            "+55 (83) 8765 4321",
            "8387654321",
            "83 87654321",
            "838765 4321",
            "aa aaaa aaaa",
            " ",
            ""
        ]

        self.validPhoneNumbers = []
        self.validPhoneNumbers.extend(self.validCellPhoneNumbers)
        self.validPhoneNumbers.extend(self.validLandlinePhoneNumbers)

        self.invalidPhoneNumbers = [] 
        self.invalidPhoneNumbers.extend(self.invalidCellPhoneNumbers)
        self.invalidPhoneNumbers.extend(self.invalidLandlinePhoneNumbers)

    
    
    def test_isBrazilianCellPhoneNumber(self):
        for cellphone in self.validCellPhoneNumbers:
            phoneValidator = BrazilianPhoneValidator(cellphone)
            self.assertTrue(phoneValidator.isBrazilianCellPhoneNumber())
        
        for cellphone in self.invalidCellPhoneNumbers:
            phoneValidator = BrazilianPhoneValidator(cellphone)
            self.assertFalse(phoneValidator.isBrazilianCellPhoneNumber()) 

        for landlinephone in self.validLandlinePhoneNumbers:
            phoneValidator = BrazilianPhoneValidator(landlinephone)
            self.assertFalse(phoneValidator.isBrazilianCellPhoneNumber()) 
    

    def test_isBrazilianLandlinePhoneNumber(self):
        for landlinephone in self.validLandlinePhoneNumbers:
            phoneValidator = BrazilianPhoneValidator(landlinephone)
            self.assertTrue(phoneValidator.isBrazilianLandlinePhoneNumber())

        for landlinephone in self.invalidLandlinePhoneNumbers:
            phoneValidator = BrazilianPhoneValidator(landlinephone)
            self.assertFalse(phoneValidator.isBrazilianLandlinePhoneNumber())

        for cellphone in self.validCellPhoneNumbers:
            phoneValidator = BrazilianPhoneValidator(cellphone)
            self.assertFalse(phoneValidator.isBrazilianLandlinePhoneNumber())
    

    def test_isBrazilianPhoneNumber(self):
        for phone in self.validPhoneNumbers:
            phoneValidator = BrazilianPhoneValidator(phone)
            self.assertTrue(phoneValidator.isBrazilianPhoneNumber())

        for phone in self.invalidPhoneNumbers:
            phoneValidator = BrazilianPhoneValidator(phone)
            self.assertFalse(phoneValidator.isBrazilianPhoneNumber())