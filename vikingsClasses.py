import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength
    
    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat" # and s/he went to Valhalla

# Saxon

class Saxon(Soldier):
    # This is not needed since it overwrite the Soldier.__init()__ without adding any extra functionality
    """
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)
    """

    def receiveDamage(self, damage):
        # your code here
        super().receiveDamage(damage)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking:Viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon:Saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def getRandomViking(self):
        if len(self.vikingArmy) > 0:
            # Select a random viking by finding a random int from 0 until the len of vikingArmy - 1
            return self.vikingArmy[random.randint(0, len(self.vikingArmy) - 1)]
        else:
            # In case vikingArmy is empty we return False 
            return False

    def getRandomSaxon(self):
        if len(self.saxonArmy) > 0:
            # Select a random saxon by finding a random int from 0 until the len of saxonArmy - 1
            return  self.saxonArmy[random.randint(0, len(self.saxonArmy) - 1)]
        else:
            # In case saxonArmy is empty we return False 
            return False

    def vikingAttack(self):
        # your code here
        # Get a Random Viking and a Random Saxon
        sel_viking = self.getRandomViking()
        if sel_viking == False:
            print("\nThere are no Vikings left to attack")
            return False

        sel_saxon = self.getRandomSaxon()
        if sel_saxon == False:
            print("\nThere are no Saxons left to defend")
            return False

        # Let's show who is fighting
        print(f"\nViking {sel_viking.name} entered in combat with a Saxon")

        # Selected saxon receives as much damage as the strength of the viking (returned by the methiod attack)
        result = sel_saxon.receiveDamage(sel_viking.attack())
        """ Previous line does this 2 operations:
        damage = sel_viking.attack()
        result = sel_saxon.receiveDamage(damage)
        """
        print(result)
        
        # If the saxon's health is 0 or less we remove him from saxonArmy
        if sel_saxon.health <= 0:
            del self.saxonArmy[self.saxonArmy.index(sel_saxon)]            
            print(f"A Saxon was removed from the Saxon Army ({len(self.saxonArmy)} left)")
        else:
            print(f"The Saxon survived ({sel_saxon.health} health point left)")

        # Return result of Saxon.receiveDamage()
        return result
    
    def saxonAttack(self):
        # your code here
        # Get a Random Saxon and a Random Viking
        sel_saxon = self.getRandomSaxon()
        if sel_saxon == False:
            print("\nThere are no Saxons left to attack")
            return False

        sel_viking = self.getRandomViking()
        if sel_viking == False:
            print("\nThere are no Vikings left to defend")
            return False

        # Let's show who is fighting
        print(f"\nA Saxon entered in combat with {sel_viking.name}")

        # Selected saxon receives as much damage as the strength of the viking (returned by the methiod attack)
        result = sel_viking.receiveDamage(sel_saxon.attack())
        """ Previous line does this 2 operations:
        damage = sel_saxon.attack()
        result = sel_viking.receiveDamage(damage)
        """
        print(result)
        
        # If the vikings's health is 0 or less we remove him from vikingArmy
        if sel_viking.health <= 0:
            del self.vikingArmy[self.vikingArmy.index(sel_viking)]
            print(f"{sel_viking.name} was removed from the Viking Army ({len(self.vikingArmy)} Vikings left)")
        else:
            print(f"{sel_viking.name} survived ({sel_viking.health} health point left)")

        # Return result of Saxon.receiveDamage()
        return result
    
    def showStatus(self):
        # your code here
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0: 
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
    def getStatus(self):
        # Extra method to get the status in a way that can be used in the main game
        # It returns a tuple with (GameOver, VikingWin) 
        #   GameOver is a Bool (True game finished, False not finished)
        #   VikingWin is a Bool (True means vikins won, False mean Vikings not won)
        if len(self.saxonArmy) == 0:
            return (True, True) # Vikings Won
        elif len(self.vikingArmy) == 0: 
            return (True, False) # Saxon Won
        else:
            return (False, False) # Game not finished

"""
vwi = War()
vwi.addViking(Viking(name="Raganar", health=100, strength=70))
vwi.addViking(Viking(name="Raganar2", health=90, strength=80))
vwi.addViking(Viking(name="Bjorn", health=80, strength=90))
vwi.addViking(Viking(name="Bjorn2", health=70, strength=100))
vwi.addSaxon(Saxon(health=100, strength=70))
vwi.addSaxon(Saxon(health=90, strength=80))
vwi.addSaxon(Saxon(health=80, strength=90))
vwi.addSaxon(Saxon(health=70, strength=100))

for i in range(10):
    vwi.vikingAttack()
    vwi.saxonAttack()
    print("\n" + vwi.showStatus())
"""