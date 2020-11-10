class Vampire(NPC):

    def __init__(self):
        super.__init__()

    def update(self):
        self.observer.update()
