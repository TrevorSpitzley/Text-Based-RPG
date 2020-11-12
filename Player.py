import random
from HersheyKiss import HersheyKiss
from SourStraw import SourStraw
from ChocolateBar import ChocolateBar
from NerdBomb import NerdBomb

class Player():

    def __init__(self):
        self.health_points = random.randint(100, 125)
        self.attack_mod = random.randint(10, 20)
        self.weapons_list = []
        self.generate_weapons()

    def print_stats(self):
        print('You currently have {} health points and your attack strength is {}!\n'.format(self.health_points, self.attack_mod))

    def update_weapons(self, weapon):
        if weapon.uses > 0:
            weapon.uses -= 1
        if weapon.uses <= 0:
            self.weapons_list.remove(weapon)

    def update_uses(self, weapon):
        pass
        # if weapon.uses > 0, minus 1
        # else, remove weapon


    def generate_weapons(self):
        for i in range(10):
            # Introducing psuedo probability
            num = random.randint(0,10)
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
        self.health_points -= monster.attack_strength

    def print_weapons(self):
        for weapon in self.weapons_list:
            print('{}: {}, {} uses left.\n'.format(self.weapons_list.index(weapon), weapon.name, weapon.uses))
