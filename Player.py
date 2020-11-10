import random
import HersheyKiss
import SourStraw
import ChocolateBar
import NerdBomb

class Player():

    def __init__(self):
        self.health_points = random.randint(100, 125)
        self.attack_mod = random.randint(10, 20)
        # Is this allowed? Or even a thing?
        self.weapons_list = [None] * 10
        self.generate_weapons()

    def generate_weapon(self):
        for i in range(10)
        # Introducing psuedo probability
        if num < 3:
            h = HersheyKiss()
            self.weapons_list.append(h)
        elif num < 6:
            s = SourStraw()
            self.weapons_list.append(s)
        elif num < 8:
            c = ChocolateBar()
            self.weapons_list.append(c)
        else:
            n = NerdBomb()
            self.weapons_list.append(n)

    def get_hit(self, monster):
        pass
