import csv

from random import *


class Weapon(object):
    min_d = 1
    max_d = 1
    type = None

    def __init__(self):
        pass

    def hit_chance(self):
        if self.type == 'Heavy':
            return 30
        elif self.type == 'Light':
            return 80
        elif self.type == 'Medium':
            return 60
        elif self.type == 'Ranged':
            return 50

    def attack(self):
        return randint(self.min_d, self.max_d)

    def __str__(self):
        return "{}".format(self.__class__.__name__)


class Sword(Weapon):
    min_d = 2
    max_d = 5
    type = "Medium"


class Halberd(Weapon):
    min_d = 8
    max_d = 18
    type = 'Heavy'


class Warhammer(Weapon):
    min_d = 4
    max_d = 6
    type = "Light"

    def attack(self):
        return randint(self.min_d, self.max_d) + 1


class Short_Bow(Weapon):
    min_d = 1
    max_d = 3
    type = "Ranged"


if __name__ == "__main__":
    s = Sword()
    h = Halberd()
    w = Warhammer()
    b = Short_Bow()
    weapon_tup = (s, h, w, b,)

    for _ in range(0, 10):
        weapon = choice(weapon_tup)

        if weapon.hit_chance() >= randint(1, 101):
            combat_dict = {'weapon': weapon.__str__(), 'hit/miss': "Hit!", 'damage': weapon.attack()}
        else:
            combat_dict = {'weapon': weapon.__str__(), 'hit/miss': "Miss!", 'damage': 'Dodged'}

        print(combat_dict)
