# Date: 26/03/2022
# Name: FIT 9136
# Description: Pokemon class describes a Pokemon. It has leveling and evolving characteristics such as attack, defense, health, and some behaviros such as train, attack_up, defense_up, and health_up, etc.

class Pokemon(object):
    # difine class variables.
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

   
    def __init__(self, name, level = 5):
        """
            argument: name:str, level:int
        """
        self.name = name
        self.level = level

    def train(self):
        """    
            purpose: improve the level and increase the value of other attributes via traning.      
            return: return the level
        """
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level


    def attack_up(self):
        """    
            purpose: increase the value of attack.       
            return: return the attack value
        """
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        """        
            purpose: increase the value of defense.     
            return: return the defense value
        """
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        """    
            purpose: increase the value of health.       
            return: return the health value
        """
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        """   
            purpose: increase the value of health, attack, defense, and evolve.    
        """
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10


    def __str__(self):
        """  
            purpose: print out pokemon's name, p_type, and level.      
        """
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

    

"""
    Grass_Pokemon is a class inherited from Pokemon class.

    Attribute:
        attack: int
        defense: int
        health: int
"""
class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    
    def update(self):
        """   
            purpose: increase the value of health, attack, defense, and evolve.    
        """
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        """   
            purpose: define a p_moves attribute: list    
        """
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]
    
    def action(self):
        """   
            return: a str    
        """
        return f"{self.name} knows a lot of different moves!"


# Create a instance "Belle"
p1 = Grass_Pokemon("Belle")
