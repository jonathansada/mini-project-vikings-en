from vikingsClasses import *
import random
import time

## TODO ##
# Fix instructions
# Viking Names
# Computer randomly selecting army length
# Set winner as Vikings
# Showing count of wins

viking_names = ["Arne", "Birger", "Bjørn", "Bo", "Erik", "Frode", "Gorm", "Halfdan", "Harald", "Knud", "Kåre", "Leif", "Njal", "Roar", "Rune", "Sten", "Skarde", "Sune", "Svend", "Troels", "Toke", "Torsten", "Trygve", "Ulf", "Ødger", "Åge", "Astrid", "Bodil", "Frida", "Gertrud", "Gro", "Estrid", "Hilda", "Gudrun", "Gunhild", "Helga", "Inga", "Liv", "Randi", "Signe", "Sigrid", "Revna", "Sif", "Tora", "Tove", "Thyra", "Thurid", "Yrsa", "Ulfhild", "Åse"]
p1_name = p2_name = ""
pvikings = 1

# Function that asks the user to introduce a value and only return if is in the valid values (id any)
def getStringUserInput(message, valid_values = []):
    uinput = input(message)
    if uinput in valid_values or valid_values==[]:
        return uinput
    else:
        # Recursive method
        return getStringUserInput(message, valid_values)

# Function that asks the user to introduce a value and only return it when is a number and/or is in the valid values
def getNumericUserInput(message, valid_values = []):
    uinput = input(message)
    if uinput.isnumeric() and (int(uinput) in valid_values or valid_values==[]):
        return int(uinput)
    else: 
        # Recursive method
        return getNumericUserInput(message, valid_values)

def getVikingsPlayer():
    global pvikings, p1_name, p2_name
    return p1_name if pvikings == 1 else p2_name

def getSaxonsPlayer():
    global pvikings, p1_name, p2_name
    return p1_name if pvikings == 2 else p2_name

"""
def get_viking_names()
    global viking_names
    random.sample(viking_names, 100)
"""

#####
# Script Start
#####

# Ask for the number of players
numPlayers = getNumericUserInput("How many players will play? (1 or 2): ", [1, 2])

# Name the players
p1_name = input(f"\nIntroduce Player 1 name: ")
if numPlayers == 2:
    p2_name = uinput = input(f"Introduce Player 2 name: ")
else:
    p2_name = "Computer"

# Select who plays with Vikings
pvikings = random.randint(1,2)
print(f"\n{getVikingsPlayer()} will start playing as Vikings")
print(f"{getSaxonsPlayer()} will start playing as Saxons")
    
print("\nGame Starts!")
playmore = ''
while playmore != 'n':
    # Show instructions
    print("You will have 1000 points to be split in the number of Vikings/Saxosn you decice (as more Soldiers you have less damage they get)")
    
    # Ask the users for the number of soldiers
    num_vikings = getNumericUserInput(f"\n{getVikingsPlayer()} - How many Vikings do you want in your Army? ")
    num_saxons = getNumericUserInput(f"{getSaxonsPlayer()} - How many Saxons do you want in your Army? ")

    # Instance War
    vikingwar = War()
    
    # Fill the Armies
    [vikingwar.addViking(Viking(name="Raganar", health=int(1000 / num_vikings), strength=random.randint(70, 120))) for num in range(0, num_vikings)]
    [vikingwar.addSaxon(Saxon(health=int(1000 / num_saxons), strength=random.randint(70, 120))) for num in range(0, num_saxons)]

    # Run the War
    gamestatus = (False, False)
    while gamestatus[0] == False:
        vikingwar.vikingAttack()
        vikingwar.saxonAttack()
        print("\n" + vikingwar.showStatus())
        gamestatus = vikingwar.getStatus()
        time.sleep(1)
    
    if(gamestatus[1] == True): # Vikings Won
        print(f"\n{getVikingsPlayer()} - Won this time!")
    else:
        print(f"\n{getSaxonsPlayer()} - Won this time!")

    playmore = getStringUserInput("\nWould you like to play another? (y or n): ", valid_values = ["y", "n"])