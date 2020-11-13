class Observable():

    def __init__(self):
        self.observer = None

    def add_observer(self, observer):
        self.observer = observer
        #if observer not in self.observers:
            #self.observers.append(observer)

    def remove_observer(self, observer):
        self.observer = None
        #if observer in self.observers:
            #self.observer.remove(observer)

    #def remove_all_observers(self):
        #self.observers = []

    def update(self, name=None):
        #for observer in obersvers:
        if self.observer:
            self.observer.update()
