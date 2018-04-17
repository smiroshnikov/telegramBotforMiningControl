# difference between class variables and instance variables

class Employee:
    # class variable
    raise_amount = 1.04
    """
    here is an example for class attribute that we  want to be same for every instance 
    e.g total number of employees 
    """
    employee_head_count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@sm.com"

        Employee.employee_head_count += 1 # this will increase with every new class instance

    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)  # here is a usage , is it convenient ?

        """ when apply raise methoid is called if will check if
        when we try to access an attribute of an instance it first checks if an instance contains that 
        attribute , if it doesnt it will look if that class or class it inherits from contains that attribute   
        """
        self.pay = int(self.pay * self.raise_amount)  # same as the line above, but self.raise_amount is better
        """ it will give us the ability to chenage raise_amout per instance , which is more flexible """


if __name__ == "__main__":
    bob = Employee("Bob", "Bobson", 1)
    muki = Employee("Muki", "Koen", 100000)
    print(bob.email)
    print(muki.fullname())  # is the same as Employee.fullname(muki), here i am just calling and instance
    print(Employee.fullname(muki))
    print(muki.pay)
    muki.apply_raise()
    print(muki.pay)
    # printing namespsce
    print(bob.__dict__)  # bob instance does not contain raise_amount attribute but ...
    print(Employee.__dict__)
    print(Employee.employee_head_count)
