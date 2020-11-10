import random as rnd

class NerdBomb(Weapon):

    def __init__(self):
        super.__init__(rnd.uniform(3.5, 5.0))
        self.name = "NerdBomb"
        self.uses = 1
