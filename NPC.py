from Observable import Observable

class NPC(Observable):

    def __init__(self, x, y):
        super().__init__()
        self.health_points = x
        self.attack_strength = y

    def check(self, player):
        if self.health_points > 0:
            print('You have hit a {}! It now has {} health points left!\n'.format(self.name, self.health_points))
        if self.health_points <= 0:
            print('Congratulations, you have killed a {}!\n'.format(self.name))
            print('The {} you just killed has now turned back into a Person. Hooray!\n'.format(self.name))
            self.update()
