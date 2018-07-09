from operator import attrgetter
from random import random

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<name: %s, age: %s>" % (self.name, self.age)


jack = Person("Jack", 19)
adam = Person("Adam", 43)
becky = Person("Becky", 11)
people = [jack, adam, becky]


def byName_key(person):
    return person.name

# people = sorted(people)
# people = sorted(people, key=byName_key, reverse=True)
# people = sorted(people, key=attrgetter('name'))
people = sorted(people, key=attrgetter('age'))
print people


class Snake(object):
    def __init__(self, name, toxicity, aggression):
        self.name = name
        self.toxicity = toxicity
        self.aggression = aggression

    def __repr__(self):
        return "<%s>" % self.name


gardenSnake = Snake("gardenSnake", 10, 0.1)
rattleSnake = Snake("rattleSnake", 100, 0.25)
kingCobra = Snake("kingCobra", 50, 1.0)
snakes = [gardenSnake, rattleSnake, kingCobra]

def byDangerous_key(snake):
    return snake.toxicity * snake.aggression

def byRandom_key(snake):
    return random()

# print sorted(snakes, key=byDangerous_key)
print sorted(snakes, key=byRandom_key)
