import random as rnd

class Zombie(NPC):
    
    # Will doing this for the super.init make each zombie have the same attack and health?
    # health = rnd.randint(50, 100)
    # attack = rnd.randint(0, 10)

    def __init__(self):
        super.__init__(rnd.randint(50, 100), rnd.randint(0, 10))
        self.name = "Zombie"

    def get_hit(weapon, player):
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
