import converters
print((converters.kg_to_lbs(50)))

def lbs_to_kg(weight):
    return weight*0.45
def kg_to_lbs (weight):
    return weight/0.45

import converters
from converters import kg_to_lbs
print(kg_to_lbs(34))

from utils import find_max
numbers = [1,4,778,9,2,3,5]
maximum = find_max(numbers)
print(maximum)

def find_max (numbers):
    maximum = numbers [0]
    for number in numbers:
        if number>maximum:
         maximum=number
    return maximum

