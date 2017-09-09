# In this module we will retrieve data from our json file using json.load()


import json

filename = 'numbers.json'
with open(filename, 'r') as f:
    numbers = json.load(f)

print(numbers)
