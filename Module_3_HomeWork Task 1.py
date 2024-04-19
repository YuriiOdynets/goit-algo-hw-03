#Task №1

from datetime import datetime
#Function that returns datetime object and handles ValuError and TypeError caused by unsupported input data
def string_to_date(date_string):
    try:
        return datetime.strptime(date_string, '%Y-%m-%d').date()
    except (ValueError,TypeError):
        print(f'"{date_string}" is not a valid date')
#Calculates day difference between today and entered date
def get_days_from_today(date):
    input_date=string_to_date(date)
    if input_date is None:
        return None
    else:
        day_diff=(datetime.today().date()- input_date).days
        return day_diff
        
days_difference = get_days_from_today('2024-04-16')
print(days_difference)

