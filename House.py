import random

class House(Observer):

    def __init__(self, x, y):
        self.x_axis = x
        self.y_axis = y
        self.num_monsters = random.randint(0, 10)
        self.location = [x, y]
        self.monsters = []
        self.generate_monsters()

    def generate_monsters(self, num):
        if num == 1:
            v = vampire()
            v.add_observer(self)
            self.monsters.append(v)
    
    def lose_monster(self):
        if self.num_monsters > 0:
            self.num_monsters -= 1

    def update(self, monster):
        # Check if 0, house finished
            # Decrement num monsters
            self.monsters.remove(monster)
