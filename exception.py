# In this module we will learn about Exception handling in python

# Handling zero division error
print("Give me two numbers and I will divide them.")
try:
    x = int(input("Enter the first number :"))
    y = int(input("Enter the second number :"))
    z = x/y
except ZeroDivisionError:
    print("cant divide by zero")
else:
    # the else block works when the try block is executed successfully
    print(z)


# Handling the file not found error
filename = 'alice.txt'

try:
    with open(filename, 'r') as f:
        contents = f.read()
except:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

# Analyzing text
filename = 'resources/chapter_10/alice.txt'

try:
    with open(filename, 'r') as f:
        contents = f.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print("The file alice.txt has about " + str(num_words) + " words.")
