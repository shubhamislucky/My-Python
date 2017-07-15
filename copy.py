from sys import argv
from os.path import exists

# in this program we will copy the contents of one file to another

# we are again using command line arguments
script, from_file, to_file = argv

print("In this program we are going to copy the contents of one file to another \n")

print("opening both files")
file1 = open(from_file)
file2 = open(to_file, 'w')

data = file1.read()

print(f"Does the destination file exists? {exists(to_file)}")
print(f"the input file is {len(data)} bytes long")

file2.write(data)

print("\n the task is done , let's close the files now")

file1.close()
file2.close()

