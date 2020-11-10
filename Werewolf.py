import random as rnd

class Werewolf(NPC):
    
    # Will doing this for the super.init make each Werewolf have the same attack and health?
    # health = 200
    # attack = rnd.randint(0, 40)

    def __init__(self):
        super.__init__(rnd.randint(0, 40), 200)
        self.name = "Werewolf"

    def get_hit(weapon, player):
        if weapon.name == "ChocolateBars":
            return
        elif weapon.name == "HersheyKisses":
            self.health_points -= (weapon.attack_mod * player.attack_mod)
        elif weapon.name == "SourStraws":
            return 
        elif weapon.name == "NerdBombs":
            self.health_points -= (weapon.attack_mod * player.attack_mod)
        else:
            return

    def update(self):
        self.observer.update()
