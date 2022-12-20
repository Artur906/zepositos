



from validators import BrazilianPhoneValidator

phoneValue = "83 0800 2141"
phoneValidator = BrazilianPhoneValidator(phoneValue)

print(phoneValidator.isBrazilianLandlinePhoneNumber())
