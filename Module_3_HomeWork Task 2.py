#Task №2

import random
#Function that defines set of numbers in certain range. Set is sorted via transformation to list
def get_numbers_ticket(min, max, quantity):
        set_of_numbers=set()
        while len(set_of_numbers) < quantity:
            set_of_numbers.add(random.randint(min,max))
        else:
            sorted_list=sorted(set_of_numbers)
            return sorted_list
#Allows user to input configuration values and returns result of get_numbers_ticket function
try: 
    min=int(input('Enter the minimum value: '))
    max=int(input('Enter the maximum value: '))
    quantity=int(input('Enter quantity: '))
    winning_combination=get_numbers_ticket(min,max,quantity)
    if winning_combination:
         print("Ваші лотерейні числа: ", winning_combination)
except ValueError:
    print("Invalid input. Please enter valid integer values.")