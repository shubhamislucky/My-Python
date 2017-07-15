# let's make a fun game using if and else

print("""
    You are in a dark room with two doors.
    Do you go through door #1 or door #2?
    """)
door = int(input("> "))

if door == 1:
    print("""
    There is a bear here eating cheesecake.
    What do you do?
    1. Take the cake
    2. Scream at the bear
    """)

    bear = int(input("> "))
    if bear is 1:
        print("Bear eats your head off. Well done!")
    elif bear is 2:
        print("Bear eats your leg off. Well done!")
    else:
        print(f"Well doing {bear} is probably better")
        print("bear runs away")

elif door == 2:
    print("""
        You find yourself in a room filled with beautiful girls
        What do you do?
        1. Kiss the most beautiful girl in the room?
        2. Slap the most ugly girl in the room?
        3. Hug the most lonely girl in the room?
        """)
    girl = int(input("> "))
    if girl == 1:
        print("The girl turns out to be a boy wearing makeup")
    elif girl == 2:
        print("Her father was in the other room, you are a dead man now !")
    elif girl is 3:
        print("She falls in love with you, madly.\nShe wants you all for herself and so she kills your family and friends\nand takes you on a lonely island.")
    else:
        print("You get a superpower and become a shitty persone doing shit allover the world")

else:
    print("you stumble around and fall on a knife and die. Good job")
