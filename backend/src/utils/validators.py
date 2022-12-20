import re

# dica: vaiaveis ou funcoes que comecam com __ (ex:__phoneNumber) são privadas no python.
# landline = telefone Fixo em ingles.

class BrazilianPhoneValidator:
    __cellRegex     = "^[0-9]{2} 9[0-9]{4} [0-9]{4}$"
    __landlineRegex = "^[0-9]{2} [0-8]{1}[0-9]{3} [0-9]{4}$"

    def __init__(self, number):
        self.__phoneNumber = number

    def isBrazilianPhoneNumber(self):
        if (self.isBrazilianCellPhoneNumber() or self.isBrazilianLandlinePhoneNumber()):
            return True
        else:
            return False

    def isBrazilianCellPhoneNumber(self):
        return self.__phoneRegexMatch(self.__cellRegex)

    def isBrazilianLandlinePhoneNumber(self):
        return self.__phoneRegexMatch(self.__landlineRegex)

    def __phoneRegexMatch(self, phoneRegex):
        pattern = re.compile(phoneRegex, re.I)
        match = pattern.match(str(self.__phoneNumber))
        return bool(match)
