from Observable import Observable

class NPC(Observable):

    def __init__(self, x, y):
        super().__init__()
        self.health_points = x
        self.attack_strength = y

    def get_health(self):
        return self.health_points

    def get_attack(self):
        return self.attack_strength
