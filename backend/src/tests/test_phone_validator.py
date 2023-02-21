import unittest
from src.utils.validators import BrazilianPhoneValidator

class TestBrazilianPhoneValidator(unittest.TestCase):
    def setUp(self):

        self.validCellPhones = [
            "81 98765 4321",
            "83 92646 2141",
            "11 91111 1111"
        ]
        self.validLandlinePhones = [
            "81 8765 4321",
            "83 0800 2141",
            "11 1111 1111"
        ]
        
        self.invalidCellPhones = [
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
        self.invalidLandlinePhones = [
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

        self.validPhones = []
        self.validPhones.extend(self.validCellPhones)
        self.validPhones.extend(self.validLandlinePhones)

        self.invalidPhones = [] 
        self.invalidPhones.extend(self.invalidCellPhones)
        self.invalidPhones.extend(self.invalidLandlinePhones)

    
    
    def test_validCellPhoneNumbers(self):
        for validCellPhone in self.validCellPhones:
            phoneValidator = BrazilianPhoneValidator(validCellPhone)
            self.assertTrue(phoneValidator.isCellPhone())    
    
    def test_invalidCellPhoneNumbers(self):
        for invalidCellPhone in self.invalidCellPhones:
            phoneValidator = BrazilianPhoneValidator(invalidCellPhone)
            self.assertFalse(phoneValidator.isCellPhone()) 
        for validLandlinePhone in self.validLandlinePhones:
            phoneValidator = BrazilianPhoneValidator(validLandlinePhone)
            self.assertFalse(phoneValidator.isCellPhone()) 


    def test_validLandlinePhoneNumbers(self):
        for validLandlinePhone in self.validLandlinePhones:
            phoneValidator = BrazilianPhoneValidator(validLandlinePhone)
            self.assertTrue(phoneValidator.isLandlinePhone())

    def test_invalidLandlinePhoneNumbers(self):
        for invalidLandlinePhone in self.invalidLandlinePhones:
            phoneValidator = BrazilianPhoneValidator(invalidLandlinePhone)
            self.assertFalse(phoneValidator.isLandlinePhone())
        for validCellPhone in self.validCellPhones:
            phoneValidator = BrazilianPhoneValidator(validCellPhone)
            self.assertFalse(phoneValidator.isLandlinePhone())
 

    def test_validPhoneNumbers(self):
        for validPhone in self.validPhones:
            phoneValidator = BrazilianPhoneValidator(validPhone)
            self.assertTrue(phoneValidator.isPhone())

    def test_invalidPhoneNumbers(self):
        for invalidPhone in self.invalidPhones:
            phoneValidator = BrazilianPhoneValidator(invalidPhone)
            self.assertFalse(phoneValidator.isPhone())