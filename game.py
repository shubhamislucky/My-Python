# let's make a game
from sys import exit

def start():
    print("==============================")
    print("\tlet's play a game")
    print("==============================\n")
    print("""
        You are in a dark room.
        There are two doors to your 'left' and 'right'.
        Which one do you take?
        """)
    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        girl_room()
    else:
        dead("You take a knife and cut your own throat.")

def bear_room():
    print("""
        There's a bear here !
        He is eating honey.
        What do you do?
        1. take his honey
        2. taunt the bear
        3. dance like a zombie
        """)
    choice = input("> ")

    if "honey" in choice:
        print("bear eats your head off")
        dead("you stupid ! you can not steal honey from a bear.")
    elif "taunt" in choice:
        print("bear eats your leg off")
        dead("seriously? are you kidding me. you are so dead.")
    elif "dance" in choice:
        print("Now that's a smart choice.")
        print("bears moves away from the door")
        gold_room()
    else:
        print("You are just dumb. Accept it and move on !")
        exit(0)

def girl_room():
    print("""
        There are three beautiful girls in this room.
        First girl is the most beautiful of the three.
        Second girl is standing nude.
        Third girl is the cutest girl in entire world.
        Which girl do you talk to ?
        """)
    choice = input("> ")
    if "first" in choice:
        print("She is completely retarded.")
        dead("While kissing you she draws out a knife and kills you.")
    elif "second" in choice:
        print("Well done !")
        print("You have sex with the girl.")
        print("She loves you forever.")
        exit(0)
    elif "third" in choice:
        print("Although she looks cute, but she is the most evil of all")
        print("She imprisones you and taunts you for the rest of your life")
        print("She kisses you on weekends")
        dead("Regret your choice!")
    else:
        dead("all three girls unite in order to ruin your life")

def gold_room():
    print("""
        This room is filled with gold.
        How much gold do you take?
        """)
    try:
        choice = int(input("> "))
    except:
        print("do you even know how to write a number? go fuck yourself")
        exit(0)
    if choice < 10000:
        print("well done ! you shall have your gold.")
        exit(0)
    elif choice > 10000:
        print("There was a dragon burried under the gold.")
        print("You took a lot of it so it got uncoverd.")
        dead("You are dead")
    else:
        print("You are just a big disappointment")

def dead(why):
    print(why, " ,Well done !")
    exit(0)

start()
