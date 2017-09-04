# Moving on with files

# Let's write code which finds out if someone's b'day is contained in first million digits of pi
filename = 'resources/chapter_10/pi_million_digits.txt'

with open(filename, 'r') as f:
    lines = f.readlines()

pi = ''
for line in lines:
    pi += line.strip()

birthday = input("Enter your birthday, in the form of ddmmyy :")
if birthday in pi:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appears in the first million digits of pi!")


# Writing to a file
filename = 'programming.txt'

with open(filename, 'w') as f:
    f.write("I love programming.\n")
    f.write("I love creating new games.\n")

# Appending to a file
with open(filename, 'a') as f:
    f.write("I also love creating apps that can run in a browser.\n")
    f.write("I love going to gym.\n")
