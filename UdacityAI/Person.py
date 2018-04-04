# keep repeating
# Superhero inherits from  Person and overwrites method in person

class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print("My real name is {}  и я обычный еблан с джавой".format(self.name))


class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)  # what does this line mean ?
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print("...And I am {}".format(self.hero_name))


maxim = Person("Max Smirnoff")
maxim.reveal_identity()
sergei = SuperHero("Sergei Miroshnikov ", "MorbusBorbus")
sergei.reveal_identity()
