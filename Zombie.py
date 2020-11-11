from NPC import NPC
from Observable import Observable
import random as rnd

class Zombie(NPC):
    
    def __init__(self):
        super().__init__(rnd.randint(50, 100), rnd.randint(0, 10))
        self.name = "Zombie"

    def get_hit(self, weapon, player):
        if weapon.name == "ChocolateBars":
            self.health_points -= (weapon.attack_mod * player.attack_mod)
        elif weapon.name == "HersheyKisses":
            self.health_points -= (weapon.attack_mod * player.attack_mod)
        elif weapon.name == "SourStraws":
            self.health_points -= (2 * (weapon.attack_mod * player.attack_mod))
        elif weapon.name == "NerdBombs":
            self.health_points -= (weapon.attack_mod * player.attack_mod)
        else:
            return

    def update(self):
        self.observer.update()
