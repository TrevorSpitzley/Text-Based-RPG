from abc import ABCMeta, abstractmethod

class Observer(object):
    __metaclass__ = ABCMeta


    # We will implemenmt the update method in any
    # class we are using as an observer, or else
    # we cannot instantiate it or use it

    @abstractmethod
    def update(self):
        pass
