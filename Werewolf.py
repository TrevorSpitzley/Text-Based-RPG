from NPC import NPC
from Observable import Observable
import random as rnd

class Werewolf(NPC):
    
    def __init__(self):
        super().__init__(200, rnd.randint(0, 40))
        self.name = "Werewolf"

    def get_hit(self, weapon, player):
        if weapon.name == "ChocolateBars":
            return
        elif weapon.name == "HersheyKisses":
            self.health_points -= (weapon.attack_mod * player.attack_mod)
        elif weapon.name == "SourStraws":
            return 
        else:
            self.health_points -= (weapon.attack_mod * player.attack_mod)

    def update(self):
        self.observer.update()
