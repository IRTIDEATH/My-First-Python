import os

# Display starting menu
def prompt():
    print("\t\t\tWelcome to my game\n\n\
          Yout must collect all six items before fighting the boss.\n\n\
          Movies:\t'go {direction}' (travel north, south, east, or west)\n\
          \t'get {item}' (add nearby item to inventory)\n\n")
    
    input("Press any key to continue...")

# Clears screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Map
rooms = {
    'Liminal Space': {'North': 'Mirror Maze', 'South': 'Bat cavern', 'Ease': 'Bazaar'},
    'Mirror Maze': {'South': 'Liminal Space', 'Item': 'Crystal'},
    'Bat Cavern': {'North': 'Liminal Space', 'East': 'Volcano', 'Item': 'Staff'},
    'Bazaar': {'West': 'Liminal Space', 'North': 'Meat Locker', 'East': 'Dojo', 'Item': 'Altoids'},
    'Meat Locker': {'South': 'Baazar', 'East': 'Quicksand Pit', 'Item': 'fig'},
    'Quicksand Pit': {'West': 'Bat Cavern', 'Item': 'Robe'},
    'Volcano': {'West': 'Bat Cavern', 'Item': 'Elderberry'},
    'Dojo': {'West': 'Bazaar', 'Boss': 'Shadow Man'}
}

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# LIst to track inventory
inventory = []

# Track current room
current_room = "Liminal Space"

# Result of last move
msg = ""

clear()
prompt()

# Gameplay Loop
while True:

    clear()

    #  Display info player
    print(f"You are in the {current_room}\nInventory : {inventory}\n{'-' * 27}")

    # Display msg
    print(msg)

    # Item indicator
    if "Item" in rooms[current_room].keys():
        
        nearby_item = rooms[current_room]["Item"]

        if nearby_item not in inventory:
            
            if nearby_item[-1] == 's':
                print(f"You see {nearby_item}")

            elif nearby_item[0] in vowels:
                print(f"You see an {nearby_item}")

            else:
                print(f"You see a {nearby_item}")

    # Boss encounter
    if "Boss" in rooms[current_room].keys():

        # Loss
        if len(inventory) < 6:
            print(f"You lost a fight with {rooms[current_room]['Boss']}.")

        # Win
        else:
            print(f"You beat {rooms[current_room]['Boss']}!")

    # Accept player's move as input
    user_input = input("Enter your move:\n")
    
    # Splits move into word
    next_move = user_input.split(' ')

    # First word is action
    action = next_move[0].title()

    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = ' '.join(item).title()

    # Moving moving between rooms
    if action == "Go":

        try:
            current_room = rooms[current_room][direction]
            msg = f"You travel {direction}."

        except:
            msg = f"You can't go that way."

    # Picking up items
    elif action == "Get":
        
        try:
            if item == rooms[current_room]["Item"]:

                if item not in inventory:

                    inventory.append(rooms[current_room]["Item"])
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}."
                
            else:
                msg = f"Can't find {item}."
        
        except:
            msg = f"Can't find {item}."

    # Exit game
    elif action == "Exit":
        break

    # Any other commands invalid
    else:
        msg = "Invalid Command"