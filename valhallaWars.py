from vikingsClasses import *
import random
import time
import os

viking_names = ["Arne", "Birger", "Bjørn", "Bo", "Erik", "Frode", "Gorm", "Halfdan", "Harald", "Knud", "Kåre", "Leif", "Njal", "Roar", "Rune", "Sten", "Skarde", "Sune", "Svend", "Troels", "Toke", "Torsten", "Trygve", "Ulf", "Ødger", "Åge", "Astrid", "Bodil", "Frida", "Gertrud", "Gro", "Estrid", "Hilda", "Gudrun", "Gunhild", "Helga", "Inga", "Liv", "Randi", "Signe", "Sigrid", "Revna", "Sif", "Tora", "Tove", "Thyra", "Thurid", "Yrsa", "Ulfhild", "Åse"]
p1_name = p2_name = ""
p1_win = p2_win = 0
pvikings = 1

def clearScreen():
    os.system('cls||clear')

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

def get_viking_names(num_names):
    global viking_names
    names = []
    ordinal = ["st", "nd", "rd", "th"] 

    iteration = 0
    while len(names) < num_names:
        missing = num_names - len(names)
        it_names = random.sample(viking_names, missing if missing <= len(viking_names) else len(viking_names))
        names += [name + f" the {iteration + 1}{ordinal[iteration] if iteration <= 2 else ordinal[3]}" for name in it_names]
        iteration += 1

    return names

#####
# Script Start
#####
clearScreen()
# Ask for the number of players
numPlayers = getNumericUserInput("How many players will play? (1 or 2): ", [1, 2])

# Name the players
p1_name = input(f"\nIntroduce Player 1 name: ")
if numPlayers == 2:
    p2_name = uinput = input(f"Introduce Player 2 name: ")
else:
    p2_name = "Computer"
clearScreen()

# Select who plays with Vikings
pvikings = random.randint(1,2)
print(f"\n{getVikingsPlayer()} will start playing as Vikings")
print(f"{getSaxonsPlayer()} will start playing as Saxons")
    
playmore = ''
available_points = 1000
allowed_num_soldiers = list(range(1, available_points + 1))
while playmore != 'n':
    # Show instructions
    print(f"\nYou have {available_points} points to split on the amount of Vikings/Saxons you want in your army.\nThese points also represents the total health of your army so more soldiers means weaker soldiers. \nChoose wisely...")
    
    # Ask the users for the number of soldiers
    if numPlayers == 1:
        if pvikings == 1: # Computer is always player 2
            num_vikings = getNumericUserInput(f"\n{getVikingsPlayer()} - How many Vikings do you want in your Army? [1-{available_points}]: ", allowed_num_soldiers)
            num_saxons = random.randint(1, available_points) 
            print(f"Saxons will play with {num_saxons} Soldiers")
        else:
            num_vikings = random.randint(1, available_points) 
            num_saxons = getNumericUserInput(f"\n{getSaxonsPlayer()} - How many Saxons do you want in your Army? [1-{available_points}]: ", allowed_num_soldiers)
            print(f"Vikings will play with {num_vikings} Soldiers")
    else:
        num_vikings = getNumericUserInput(f"\n{getVikingsPlayer()} - How many Vikings do you want in your Army?  [1-{available_points}]: ", allowed_num_soldiers)
        num_saxons = getNumericUserInput(f"{getSaxonsPlayer()} - How many Saxons do you want in your Army? [1-{available_points}]: ", allowed_num_soldiers)

    # Instance War
    vikingwar = War()
    
    # Fill the Armies
    v_names = get_viking_names(num_vikings)
    [vikingwar.addViking(Viking(name=v_names[num], health=int(1000 / num_vikings), strength=random.randint(70, 110))) for num in range(0, num_vikings)]
    [vikingwar.addSaxon(Saxon(health=int(1000 / num_saxons), strength=random.randint(70, 120))) for num in range(0, num_saxons)]

    # Run the War
    input("\nPress Enter to start the battle ...")

    gamestatus = (False, False)
    endmatch = False
    while endmatch == False:
        clearScreen()
        v_left = f"{len(vikingwar.vikingArmy)}/{num_vikings}"
        s_left = f"{len(vikingwar.saxonArmy)}/{num_saxons}"
        print(f"P1: {p1_name}({p1_win}) - {f"{v_left} Vikings:" if pvikings == 1 else f"{s_left} Saxons"} |  P2: {p2_name}({p2_win}) - {f"{v_left} Vikings" if pvikings == 2 else f"{s_left} Saxons"}")

        if gamestatus[0] == False:
            vikingwar.vikingAttack()
            vikingwar.saxonAttack()
            gamestatus = vikingwar.getStatus()
            time.sleep(0.5)
        else:
            print("\n" + vikingwar.showStatus())
            endmatch = True
            
    
    if(gamestatus[1] == True): # Vikings Won
        print(f"\n{getVikingsPlayer()} - Won this time!")
        # If Vikings won this time no need to switch players
        #Add the winner count
        p1_win = p1_win+1 if pvikings==1 else p1_win
        p2_win = p2_win+1 if pvikings==2 else p2_win
    else:
        print(f"\n{getSaxonsPlayer()} - Won this time!")
        # If Saxon won we switch players
        pvikings = 1 if pvikings == 2 else 2
        #Add the winner count
        p1_win = p1_win+1 if pvikings==2 else p1_win
        p2_win = p2_win+1 if pvikings==1 else p2_win

    print(f"Win count: {p1_name}: {p1_win} | {p2_name}: {p2_win}")

    playmore = getStringUserInput("\nWould you like to play another? (y or n): ", valid_values = ["y", "n"])
    clearScreen()

    if playmore == "y" and gamestatus[1] == False:
        print(f"\n{getVikingsPlayer()} will play as Vikings in this match")
        print(f"{getSaxonsPlayer()} will play as Saxons in this match")
