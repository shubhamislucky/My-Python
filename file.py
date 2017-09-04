# In this script we will learn about file_handling in python
# which we already did before but let's try something new

# now this is pretty awesome

# reading an entire file
with open('test.txt', 'r') as f:
    contents = f.read()
    print(contents)

# Reading line by line
with open('test.txt', 'r') as f:
    for line in f:
        print(line.rstrip())

# Accessing files outside our project
# the ../ moves one directory up
with open('../../hello.txt') as f:
    contents = f.read()
    print()
    print(contents.rstrip())

# one more way
with open('/Users/shubhamislucky/Desktop/hello.txt') as f:
    contents = f.read()
    print(contents.rstrip())

# Making a list of lines from a file
# f.readlines() function returns a list
with open('test.txt', 'r') as f:
    contents = f.readlines()
    for item in contents:
        print(item.rstrip())

print()
sayings = ''
for item in contents:
    sayings += item.strip()

print(sayings)
print(len(sayings))

# Working with large files
filename = 'resources/chapter_10/pi_million_digits.txt'

with open(filename, 'r') as f:
    lines = f.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
