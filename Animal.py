class Animal:
    def __init__(self,name):
        self._name=name
    def info(self):
        print("Animal name: ",self._name)
class Cat(Animal):
    def sound(self):
        print(self._name," mews")

c=Cat("Kitty")
c.info()
c.sound()