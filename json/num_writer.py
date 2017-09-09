# In this module we will learn about JSON
# with json module we can dump and load simple python data structures in a file
"""
    In this module we will dump data to a file 'numbers.json' and in
    other module we will retrieve that data.
"""


import json

numbers = [1,2,3,4,5,6]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
