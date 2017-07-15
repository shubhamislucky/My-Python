# in this script we will be working with loops and lists

count = [0,1,2,3,4,5,6]
fruits = ['apples', 'bananas', 'oranges', 'strawberries', 'pineapples']
combine = [1, 'apples', 2, 'bananas', 3, 'oranges', 4, 'strawberries', 5, 'pineapples'] # we can combine types in lists

#first kind of for loop that goes through a list
for number in count:
    print(f"The number is {number}")

# let's try for in the list containing strings
for fruit in fruits:
    print(f"I am eating {fruit}")

# now we try our loop on the combined list type
for mix in combine:
    print(f"mix is a variable which contains {mix}")

# now let's build lists from scratch

elements = []

for x in range(0,10):
    print(f"Now adding {x} to our list")
    elements.append(x)

print("lets print the newly created list")

for x in elements:
    print(f"{x} ")
