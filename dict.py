# in this module we will learn about awesome dictionaries

# defining a dictionary
en_hin = {"good":"accha", "sit":"baithna", "walk":"chalna", "love":"pyar"}
# now let's check our eng-hindi dictionary
print(en_hin["good"])
print(en_hin["sit"])
print(en_hin["love"])
print(en_hin) # there is no ordering in dictionaries

# let's try to mix things up a little
grocery_list = {"mango":"Yes", "Orange":12, "Bananas":"No", "Pineapple":5}
print(grocery_list["mango"])
print(grocery_list["Orange"])
print(grocery_list["Bananas"])
print(grocery_list["Pineapple"])
print(grocery_list)

# adding a new entry to an existing dictionary
grocery_list["Guava"] = "Yes"
print(grocery_list)

# so this way we can start with an empty dictionary and add items to it as we proceed
#let's make a list of cities and their population
city = {}
city["Delhi"] = 78000
city["Mumbai"] = 80000
city["Gurgaon"] = 45000
city["Manali"] = 32000
print(city)

# we can modify our dictionary as we go
city["Mumbai"] = 81000
print(city)

# let's perform some funcitons on our dictionaries
len_city = len(city) #returns the number of key-value pairs
print(len_city)

del city["Gurgaon"] #deletes the key with its value
print(city)

print("Mumbai" in city) #returns true if the key exists in dictionary
print("Lucknow" not in city) #returns true if the key does not exists in dictionary

# iterating over a dictionary
# iterating over keys: 1st way
for keys in city:
    print(keys)

# 2nd way
for keys in city.keys():
    print(keys)

# iterating over values
for values in city.values():
    print(values)

# now let's combine both
print("\ncity " + " population")
for keys,values in zip(city.keys(),city.values()):
    print(keys, " ", values)
