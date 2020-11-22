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
            spot = self.weapons_list.index(weapon)
            del self.weapons_list[spot]
    
    def generate_random_weapon(self):
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
        print('Congratulations! A Person in the house has given you a {} to add to your weapons list!\n'.format(self.weapons_list[-1].name))

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
        if monster.name == "Person":
            print('How nice.. a Person has given you {} health points back for being awesome!'.format(-1 * monster.attack_strength))
            if (random.randint(0, 2)) == 0 and len(self.weapons_list) < 10:
                self.generate_random_weapon()

    def print_weapons(self):
        for weapon in self.weapons_list:
            print('{}: {}, {} uses left.\n'.format(self.weapons_list.index(weapon), weapon.name, weapon.uses))
