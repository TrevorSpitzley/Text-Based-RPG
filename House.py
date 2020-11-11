import random
from Observable import Observable
from Observer import Observer
from Vampire import Vampire
from Werewolf import Werewolf
from Ghoul import Ghoul
from Zombie import Zombie

class House(Observable, Observer):

    def __init__(self):
        # Multiple calls to super??
        super().__init__()
        # self.x_axis = x
        # self.y_axis = y
        self.num_monsters = random.randint(0, 10)
        # self.grid_location = [x, y]
        # self.list_location = [y, x]
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
        pass
        # Check if 0, house finished
            # Decrement num monsters
            #self.monsters.remove(monster)
