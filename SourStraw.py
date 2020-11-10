import random as rnd

class SourStraw(Weapon):

    def __init__(self):
        super.__init__(rnd.uniform(1.0, 1.75))
        self.name = "SourStraw"
        self.uses = 2
