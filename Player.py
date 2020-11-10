import random

class Player():

    def __init__(self):
        pass


    def generate_weapon(self, num):
        if num == 1:
            s = SourStraw()
            self.weapons_list.append(s)
