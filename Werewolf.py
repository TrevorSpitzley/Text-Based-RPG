from NPC import NPC
from Observable import Observable
import random as rnd

class Werewolf(NPC):
    
    def __init__(self):
        super().__init__(200, rnd.randint(0, 40))
        self.name = "Werewolf"

    def get_hit(self, weapon, player):
        if weapon.name == "ChocolateBar":
            return
        elif weapon.name == "HersheyKiss":
            self.health_points -= (weapon.attack_mod * player.attack_mod)
        elif weapon.name == "SourStraw":
            return 
        else:
            self.health_points -= (weapon.attack_mod * player.attack_mod)
        self.check(player)

    def update(self):
        self.observer.update(self)
