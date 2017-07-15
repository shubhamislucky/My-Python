# Doing things to lists

twelve_things = "apples jacket oranges car bike cellphone gun sun"
more_stuff = ['piranha', 'superman', 'batman', 'holyshit', 'cowdung', 'coding']

rand_list = twelve_things.split(' ')

print("Wait ! there are not twelve things in our list.")
print("let's add more things to our list")

while len(rand_list) != 10:
    next_item = more_stuff.pop()                                # taking out elements from more_stuff
    print(f"Adding: {next_item}")
    rand_list.append(next_item)                                 # adding more items to list
    print("Number of items present in list: ", len(rand_list))

print("There we go:")
print(rand_list)

print("let's play with our list for a little bit")

print(rand_list[1])
print(rand_list[-1])
print(rand_list.pop())
print(" ".join(rand_list))
print(' # '.join(rand_list[2:5]))
