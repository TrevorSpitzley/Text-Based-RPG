import random
from Person import Person
from Observable import Observable
from Observer import Observer
from Vampire import Vampire
from Werewolf import Werewolf
from Ghoul import Ghoul
from Zombie import Zombie

class House(Observable, Observer):

    def __init__(self):
        super().__init__()
        self.num_monsters = random.randint(0, 10)
        self.monsters = []
        self.generate_monsters()

    def show_monsters(self):
        for mon in self.monsters:
            print('There is a {} with {} health points'.format(mon.name, mon.health_points))

    def generate_monsters(self):
        for i in range(self.num_monsters):
            num = random.randint(0, 10)
            if num < 3:
                z = Zombie()
                z.add_observer(self)
                self.monsters.append(z)
            elif num < 6:
                v = Vampire()
                v.add_observer(self)
                self.monsters.append(v)
            elif num < 8:
                g = Ghoul()
                g.add_observer(self)
                self.monsters.append(g)
            else:
                w = Werewolf()
                w.add_observer(self)
                self.monsters.append(w)
    
    def lose_monster(self):
        if self.num_monsters > 0:
            self.num_monsters -= 1

    def update(self, monster):
        spot = self.monsters.index(monster)
        self.monsters[spot] = Person()
        self.num_monsters -= 1
        if self.num_monsters == 0:
            self.observer.update(self)
