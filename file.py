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
