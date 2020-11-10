import random as rnd

class ChocolateBar(Weapon):

    def __init__(self):
        super.__init__(rnd.uniform(2.0, 2.4))
        self.name = "ChocolateBar"
        self.uses = 4
