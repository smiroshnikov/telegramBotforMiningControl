class Dog(object):
    """ a sophisticated digital canine """

    def __init__(self, name, age, material='titan'):
        self.name = name
        self.age = age
        self.material = material


if __name__ == "__main__":
    Snoopy = Dog("Sn00py", 1.5)
    print(Snoopy.name + " " + Snoopy.material)
