# Date: 26/03/2022
# Name: FIT 9136
# Description: Pokemon class describes a Pokemon. It has leveling and evolving characteristics such as attack, defense, health, and some behaviros such as train, attack_up, defense_up, and health_up, etc.

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
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
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12
    
    def train(self):
        """
            modify the train method of Pokemon class
        """
        # the attack strength does not change the the level is less than 10
        if self.level < 10:
            self.update()
            self.defense_up()
            self.health_up()
            self.level = self.level + 1
            if self.level%self.evolve == 0:
                return self.level, "Evolved!"
            else:
                return self.level
        #  At level 10 and up, the attack strength increases by attack_boost
        else:
            self.update()
            self.defense_up()
            self.attack_up()
            self.health_up()
            self.level = self.level + 1
            if self.level%self.evolve == 0:
                return self.level, "Evolved!"
            else:
                return self.level

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

# create an instance "Bulby"
p2 = Grass_Pokemon("Bulby")

# create an instance "Pika"
p3 = Grass_Pokemon("Pika")
while p3.level < 10:
    p3.train()
    print(p3.level)
