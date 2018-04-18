class Worker:
    employee_counter = 0
    raise_amt = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = str.lower(first + "." + last + "@gmail.com")
        Worker.employee_counter += 1

    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    def full_details(self):
        return 'Full name : {} {} \nEmail: {} \nSalary: {}'.format(self.first, self.last, self.email, self.salary)

    def apply_raise(self):
        self.salary = int(self.raise_amt * self.salary)

    @classmethod  # class methods work with class instead of the instance
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount


if __name__ == "__main__":
    sm = Worker("Sergei", "Miroshnikov", 130000)
    mk = Worker("Muki", "Buhbut", 4500)
    print(sm.full_details())
    print(mk.full_details())
    """
    print(Worker.fullname(bob))  # this line is actually WHAT HAPPENS inside python
    """
    print(sm.raise_amt)
    print(mk.raise_amt)
    Worker.set_raise_amount(1.14)
    # this method will change CLASS VARIABLE even if i will run this on instance of the class
    # e.g sm.set_raise_amount(1.14) will change raise amount for all class instances 
    print(sm.raise_amt)
    print(mk.raise_amt)
    print(sm.salary)
    sm.apply_raise()
    print(sm.salary)
