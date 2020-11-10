class Observable(object):

    def __init__(self):
        self.observables = []

    def add_observables(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observer.remove(observer)

    def remove_all_observers(self):
        self.observers = []

    def update(self, name=None):
        for observer in obersvers:
            observer.update()
