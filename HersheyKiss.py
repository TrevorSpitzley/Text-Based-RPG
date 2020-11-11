import random as rnd
import math
from Weapon import Weapon

class HersheyKiss(Weapon):

    def __init__(self):
        super().__init__(1)
        self.name = "HersheyKiss"
        self.uses = math.inf
