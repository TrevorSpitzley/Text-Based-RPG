import random as rnd
from NPC import NPC

class Person(NPC):
    
    def __init__(self):
        super().__init__(10, rnd.randint(-20, -10))
        self.name = "Person"

    def get_hit(self, weapon, player):
        pass
