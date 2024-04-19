#Task №3

import re

def normalize_phone(raw_number):
    cleaned_number = re.sub(r'\D', '', raw_number)
    if not cleaned_number.startswith('+38') and not cleaned_number.startswith('380'):
        cleaned_number = '+38' + cleaned_number
    else:
        cleaned_number = '+' + cleaned_number
    return cleaned_number

raw_numbers = "067\\t123 4567"

print(normalize_phone(raw_numbers))