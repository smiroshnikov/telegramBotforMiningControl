class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@sm.com"

    def fullname(self):
        return '{} {} '.format(self.first, self.last)


if __name__ == "__main__":
    bob = Employee("Bob", "Bobson", 1)
    muki = Employee("Muki", "Koen", 100000)
    print(bob.email)
    print(muki.fullname())  # is the same as Employee.fullname(muki), here i am just calling and instance
    print(Employee.fullname(muki))
