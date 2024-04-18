##Task №1
#
#from datetime import datetime
##Function that returns datetime object and handles ValuError and TypeError caused by unsupported input data
#def string_to_date(date_string):
#    try:
#        return datetime.strptime(date_string, '%Y-%m-%d').date()
#    except (ValueError,TypeError):
#        print(f'"{date_string}" is not a valid date')
##Calculates day difference between today and entered date
#def get_days_from_today(date):
#    input_date=string_to_date(date)
#    if input_date is None:
#        return None
#    else:
#        day_diff=(datetime.today().date()- input_date).days
#        return day_diff
#        
#days_difference = get_days_from_today('2024-04-16')
#print(days_difference)
#
#
##Task №2
#
#import random
##Function that defines set of numbers in certain range. Set is sorted via transformation to list
#def get_numbers_ticket(min, max, quantity):
#        set_of_numbers=set()
#        while len(set_of_numbers) < quantity:
#            set_of_numbers.add(random.randint(min,max))
#        else:
#            sorted_list=sorted(set_of_numbers)
#            return sorted_list
##Allows user to input configuration values and returns result of get_numbers_ticket function
#try: 
#    min=int(input('Enter the minimum value: '))
#    max=int(input('Enter the maximum value: '))
#    quantity=int(input('Enter quantity: '))
#    winning_combination=get_numbers_ticket(min,max,quantity)
#    if winning_combination:
#         print("Ваші лотерейні числа: ", winning_combination)
#except ValueError:
#    print("Invalid input. Please enter valid integer values.")
#
##Task №3
#
#import re
#
#def normalize_phone(raw_numbers):
#    normalize_numbers=[]
#    for number in raw_numbers:
#        cleaned_number = re.sub(r'\D', '', number)
#        if not cleaned_number.startswith('+38') and not cleaned_number.startswith('380'):
#            cleaned_number = '+38' + cleaned_number
#        else:
#            cleaned_number = '+' + cleaned_number
#        normalize_numbers.append(cleaned_number)
#    return normalize_numbers
#
#
#raw_numbers = [
#    "067\\t123 4567",
#    "(095) 234-5678\\n",
#    "+380 44 123 4567",
#    "380501234567",
#    "    +38(050)123-32-34",
#    "     0503451234",
#    "(050)8889900",
#    "38050-111-22-22",
#    "38050 111 22 11   ",
#]
#normalize_numbers = normalize_phone(raw_numbers)
#print(normalize_numbers)
#
##         OR
#
#for phone in raw_numbers:
#    cleaned_number=re.sub(r'\D','',phone)
#    if not cleaned_number.startswith('+'):
#        if cleaned_number.startswith('380'):
#            cleaned_number='+'+cleaned_number
#        else:
#            cleaned_number='+38'+cleaned_number
#    print(cleaned_number)