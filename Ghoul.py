import random as rnd

class Ghoul(NPC):
    
    # Will doing this for the super.init make each Ghoul have the same attack and health?
    # health = rnd.randint(40, 80)
    # attack = rnd.randint(15, 30)

    def __init__(self):
        super.__init__(rnd.randint(40, 80), rnd.randint(15, 30))
        self.name = "Ghoul"

    def get_hit(weapon, player):
        if weapon.name == "ChocolateBars":
            self.health_points -= (weapon.attack_mod * player.attack_mod)
        elif weapon.name == "HersheyKisses":
            self.health_points -= (weapon.attack_mod * player.attack_mod)
        elif weapon.name == "SourStraws":
            self.health_points -= (2 * (weapon.attack_mod * player.attack_mod))
        elif weapon.name == "NerdBombs":
            self.health_points -= (5 * (weapon.attack_mod * player.attack_mod))
        else:
            return

    def update(self):
        self.observer.update()
