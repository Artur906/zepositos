import re

def has_field(payload, field):
    try:
        payload[field]
    except:
        return False
    return True



def brazilian_phone_number_validation_check(phone):
    expressaoCell= "^[0-9]{2} 9[0-9]{4} [0-9]{4}$"
    expressaoFixo = "^[0-9]{2} [0-8]{1}[0-9]{3} [0-9]{4}$"
    
    regexCell = re.compile(expressaoCell, re.I)
    matchCell = regexCell.match(str(phone))
    regexFixo = re.compile(expressaoFixo, re.I)
    matchFixo = regexFixo.match(str(phone))

    if(bool(matchFixo) or bool(matchCell)):
        return True
    return False


'''

validos = [
"83 92646 2141",
"83 0800 2141"
]

invalidos= [
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


for i in validos:
    print(brazilian_phone_number_validation_check(i))
print('--------')
for i in invalidos:
    print(brazilian_phone_number_validation_check(i))



'''