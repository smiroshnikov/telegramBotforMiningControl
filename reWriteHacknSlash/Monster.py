import random

# constants

COLORS = ['yellow', 'red', 'black', 'brown']
WEAPONS = ['Axe', 'Spear', 'Bow', 'Sword']


class Monster:
    """
    static class variables
    """
    min_hp = 1
    max_hp = 10
    monster_counter = 0

    def __init__(self, **kwargs):
        self.hp = random.randint(self.min_hp, self.max_hp)
        self.weapon = random.choice(WEAPONS)
        self.color = random.choice(COLORS)
        for key, value in kwargs.items():
            setattr(self, key, value)  # how unsafe is that ? I can add anything to class ? what is ther right way
        self.monster_counter += 1

    def __str__(self):
        return '{} , {} , HP : {} armed with {}'.format(self.__class__.__name__,
                                                        self.color,
                                                        self.hp,
                                                        self.weapon)

    @classmethod
    def set_hp_bounds(cls, min_hp, max_hp):
        cls.min_hp = min_hp
        cls.max_hp = max_hp

    @staticmethod
    def check_if_elite():
        if Monster.monster_counter % 10 == 0:
            return True
        return False


class Goblin(Monster):
    min_hp = 3
    max_hp = 15


if __name__ == "__main__":
    Azog = Goblin(treasure='100 gold pieces')
    print(Azog.__str__())
    print(Azog.treasure)

    Goblin.set_hp_bounds(12, 50)
    Mazog = Goblin()
    print(Mazog.__str__())
