from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):
    def make_sound(self):
        return "Roar"
    def sleep(self):
        return "Tiger is sleeping"
    def eat(self):
        return "Tiger is eating"

class Dog(Animal):
    def make_sound(self):
        return "Bark"
    def sleep(self):
        return "Dog is sleeping"
    def eat(self):
        return "Dog is eating"
    
class Monkey(Animal):
    def make_sound(self):
        return "Chatter"
    def sleep(self):
        return "Monkey is sleeping"
    def eat(self):
        return "Monkey is eating"


def animal_actions(animal):
    print(animal.make_sound())
    print(animal.sleep())
    print(animal.eat())
    print("-----")

t = Tiger()
d = Dog()
m= Monkey()
animal_actions(t)
animal_actions(d)
animal_actions(m)