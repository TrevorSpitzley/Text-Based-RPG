from NPC import NPC
from Observable import Observable
import random as rnd

class Vampire(NPC):
    
    def __init__(self):
        super().__init__(rnd.randint(100, 200), rnd.randint(10, 20))
        self.name = "Vampire"

    def get_hit(self, weapon, player):
        if weapon.name == "ChocolateBars":
            return
        elif weapon.name == "HersheyKisses":
            self.health_points -= (weapon.attack_mod * player.attack_mod)
        elif weapon.name == "SourStraws":
            self.health_points -= (weapon.attack_mod * player.attack_mod)
        elif weapon.name == "NerdBombs":
            self.health_points -= (weapon.attack_mod * player.attack_mod)
        else:
            return

    def update(self):
        self.observer.update()
