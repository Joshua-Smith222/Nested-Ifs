#task 1 code correction
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

#task 2 setting the scene
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You find a hidden treasure!")
    else:
        print("Watch your step!")

#task3
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == "proceed in the dark":
        print("Watch your step!")
    else:
        pass
else:
    pass
