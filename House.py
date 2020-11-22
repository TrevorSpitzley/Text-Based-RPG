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
        if len(self.monsters) != 0:
            for mon in self.monsters:
                if mon.name != "Person":
                    print('There is a {} with {} health points'.format(mon.name, mon.health_points))
        else:
            print('There are no monsters here! Must be your lucky day...')

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

    def is_empty(self):
        return self.num_monsters == 0

    def update(self, monster):
        spot = self.monsters.index(monster)
        self.monsters[spot] = Person()
        self.monsters[spot].add_observer(self)
        self.num_monsters -= 1
        if self.num_monsters == 0:
            self.observer.update(self)
