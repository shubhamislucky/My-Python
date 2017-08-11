# in this script we will learn about sets and frozensets
# sets are defined as unordered collection of unique elements
# sets are mutable

myset = {'apple', 'mango', 'bananas'}

print(type(myset))
print(myset)

# creating a set from scratch
myset1 = set()                        #another way of creating set
myset1.add('car')
myset1.add('ship')
myset1.add('helicopter')
myset1.add('aeroplane')
myset1.add('buggy')

print(type(myset))
print(myset)

# creating set from strings
mystring = "shubham"
myset2 = set(mystring)

print(type(myset2))
print(myset2)                        #notice that elements are not ordered

# creating set from lists
mylist = ['car', 'ship', 'aeroplane', 'ship', 'buggy']
myset3 = set(mylist)
print(type(myset3))
print(myset3)

# using for loop on sets
for x in myset3:
    print(x, end=" ")

# creating sets from tuples
mytuple = ("switzerland", "france", "italy", "san-francisco", "rome", "france", "italy")
# notice that our tuple contains duplicate elements

myset4 = set(mytuple)
print("\n", myset4)           # notice that our set now does not contain duplicate values
print(type(myset4))

# frozensets
# sets are mutable whereas frozensets are not
# frozensets don't have a function like add

myfset = frozenset(["london", "paris", "newyork"])
print(myfset)
print(type(myfset))

# now let us take a look at some set operations
# add(element)

colors = {"green", "yellow"}
colors.add("brown")
colors.add("purple")
colors.add("black")
print(colors)

# clear

colors.clear()      #all elements will be removed from a set
print(colors)

# copy

colors = {"green", "yellow", "blue", "white"}
colors2 = colors.copy()
print(colors,"\n",colors2)

# difference

colors = {"green", "yellow", "blue"}
colors2 = {"yellow", "blue", "white"}
print(colors.difference(colors2))       #returns a new set

# difference_update

colors.difference_update(colors2)
print(colors)                           # deletes the elements of colors2 form colors

# discard(element)

print(colors2)
colors2.discard("yellow")
print(colors2)

# remove(element)
# works like discard but if element is not a member of set error will be generated

print(colors2)
colors2.remove("blue")
print(colors2)

# sets have more functions like
# union(set)                       ex:- x.union(y)
# intersection(set)                ex:- x.intersection(y)
# isdisjoint(set)                  returns true if two sets have null intersection
# issubset(set)                    ex:- x.issubset(y)
# issuperset(set)                    ex:- x.issuperset(y)
# pop()                            ex:-  x.pop()
