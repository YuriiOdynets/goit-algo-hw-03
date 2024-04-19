#Task №3

import re

def normalize_phone(raw_numbers):
    normalize_numbers=[]
    for number in raw_numbers:
        cleaned_number = re.sub(r'\D', '', number)
        if not cleaned_number.startswith('+38') and not cleaned_number.startswith('380'):
            cleaned_number = '+38' + cleaned_number
        else:
            cleaned_number = '+' + cleaned_number
        normalize_numbers.append(cleaned_number)
    return normalize_numbers


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
normalize_numbers = normalize_phone(raw_numbers)
print(normalize_numbers)

#         OR

#for phone in raw_numbers:
#    cleaned_number=re.sub(r'\D','',phone)
#    if not cleaned_number.startswith('+'):
#        if cleaned_number.startswith('380'):
#            cleaned_number='+'+cleaned_number
#        else:
#            cleaned_number='+38'+cleaned_number
#    print(cleaned_number) 