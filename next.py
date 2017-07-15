from sys import argv #that's how you import stuff here

#using command line arguments
script, filename = argv

print("We are now going to truncate this file...")
myfile = open(filename, "w")
myfile.truncate() #that's how we truncate file guys

print("let us check out that the file exist in which we want to write data")

print("Now yo must enter three lines of strings so that we can write it to the next.txt file")
lfirst = input("first line > ")
lsecond = input("second line > ")
lthird = input("third line > ")

#writing to the file

myfile.write(lfirst + "\n" + lsecond + "\n" + lthird + "\n")

print("\n Now finally after doing all of the shit we close it")
myfile.close()