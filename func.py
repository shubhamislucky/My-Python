from sys import argv
from os.path import exists

script, filename = argv

def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(0)

def print_line(line_count,f):
	print(f" {line_count} : {f.readline()} ")

myfile = open(filename) # opening the file

print(f"Let us print all the data inside file > {filename} \n")

print_all(myfile)

print("Now let us rewind the file to set the pointer again to the beginnig of the file")

rewind(myfile) # if we don't rewind nothing will be printed as the pointer will be at last posintion in file

print("Now we will print the data line by line\n")

line_num = 1
print_line(line_num, myfile)

line_num = line_num + 1
print_line(line_num, myfile)

line_num = line_num + 1
print_line(line_num, myfile)

# we must close the file
myfile.close()
