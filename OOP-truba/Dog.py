from random import Random


class Dog(object):

    def __str__(self):
        return "This unit name is " + self.name \
               + " and it is " + str(self.age) + \
               " years old" + "\n" + "and it is made from " + self.material

    def __init__(self, name, age, material='titan'):
        self.name = name
        self.age = age
        self.material = material

    def initialize(self):
        print("Attempting to deploy Procaine Needle ...")
        # add random result here
        result = Random.randint(1,100)
        if result > 50+self.age:
            print("Success...")
            return True
        else:
            print("Failure...")
            return False

    def walk(self, distanse):
        print("The electric dog just walked " + str(distanse) + "km")

    def bark(self):
        print("whoof whoof")


if __name__ == "__main__":
    unit1 = Dog("bob01", 0, "3d printed aluminum")
    unit2 = Dog("bob02", 0)

    print(unit1.__str__())
    # much better than calling __str__()
    print(str(unit2))

    print(unit2.material + " vs " + unit1.material)
    unit1.walk(250)
    unit2.bark()
    unit2.initialize()