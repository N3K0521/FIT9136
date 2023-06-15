# Date: 4 Apr 2023
# Name: Huixin Wang
# Description:

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

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    # write your answers here:
    def train(self):
        if self.level < 10:
            self.update()
            self.defense_up()
            self.health_up()
            self.level = self.level + 1
            if self.level%self.evolve == 0:
                return self.level, "Evolved!"
            else:
                return self.level
        else:
            self.update()
            self.attack_up()
            self.defense_up()
            self.health_up()
            self.level = self.level + 1
            if self.level%self.evolve == 0:
                return self.level, "Evolved!"
            else:
                return self.level

#Bulby
p2 = Grass_Pokemon("Bulby")

#Pika
p3 = Grass_Pokemon("Pika")

while p3.level < 10:
    p3.train()
    print(p3.level)

