#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    else:
        print('There is nothing valuable in this location.')
    if 'map' in inventory:
        if 'north' in rooms[currentRoom]:
            print(f"The {rooms[currentRoom]['north']} is north.")
        if 'south' in rooms[currentRoom]:
            print(f"The {rooms[currentRoom]['south']} is south.")
        if 'east' in rooms[currentRoom]:
            print(f"The {rooms[currentRoom]['east']} is east.")
        if 'west' in rooms[currentRoom]:
            print(f"The {rooms[currentRoom]['west']} is west.")
    print("---------------------------")


#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : { 
                  'south' : 'Kitchen',
                  'north' : 'Courtyard',
                  'east' : 'Bedroom',
                  'west' : 'Lounge',
                  'item' : 'map'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'south' : 'Pantry'
                  },
            'Dining Room' : {
                'north' : 'Lounge',
                'item' : 'car keys'
                },
            'Study' : {
                'north' : 'Bedroom',
                'item' : 'monster',
                'prize' : "monster's head"
                },
            'Bedroom' : {
                'west' : 'Hall',
                'south' : 'Study',
            },
            'Pantry' : {
                'north' : 'Kitchen',
                'item' : 'knife',
                },
            'Courtyard' : {
                'south' : 'Hall',
                'item' : 'car'
                },
            'Lounge' : {
                'east' : 'Hall',
                'south' : 'Dining Room',
                'item' : 'key'
                }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:
    showStatus()
  
    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':  
        move = input('>')
    
    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)
  
    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            if currentRoom == 'Bedroom' and 'key' not in inventory and move[1] == 'south':
                print('You hear growls coming from that room, but thankfully it is locked. Be careful when entering!')
            else:
                currentRoom = rooms[currentRoom][move[1]]
                if currentRoom == 'Study' and 'monster' in rooms[currentRoom]['item'] and 'knife' in inventory:
                    attack = input("There is a monster do you want to use the knife to attack the monster? (yes or no) ")
                    while True:
                        if attack == 'yes':
                            print(f"Congrats you defeated the monster! You took the {rooms[currentRoom]['prize']} as your trophy.")
                            inventory.append(rooms[currentRoom]['prize'])
                            del rooms[currentRoom]['item']
                            break
                        elif attack == 'no':
                            print("Run away quick before the monster attacks.")
                            break
                        else:
                            attack = input("That is not a valid input please enter yes if you would like to attack or no if not. ")
       
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
  
    #if they type 'get' first
    if move[0] == 'get':
        #if the room contains an item, and the item is the one they want to get
        if rooms[currentRoom]['item'] == 'monster' and 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            print("You can\'t get the monster, but he looks like he is about to attack.")
        elif rooms[currentRoom]['item'] == 'car' and 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            print("You can\'t get the car. Defeat the monster first!")
        elif 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        elif 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            print("You can\'t get the monster, but he looks like he is about to attack.")

        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if currentRoom == 'Courtyard' and 'car keys' in inventory and "monster's head" in inventory:
       print("You drive away victorious with the monster's head as your trophy!")
       break
    if currentRoom == 'Study' and 'knife' not in inventory and 'monster' in rooms[currentRoom]['item']:
       print("The monster attacked you and you did not have a weapon to defend yourself. Try again.")
       break
