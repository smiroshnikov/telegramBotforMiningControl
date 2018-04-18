import datetime

""" 
this code shows difference and inplementation of @classmethod @static method and regular method
regular methods use (self) as first argument and are applied to instance of a class 
@classmethod is applied on class/class variable e.g raise_amt and receive automatic first argument as a class 
@staticmethod dont pass anythong automatically (contrary to 'self' or 'cls')and  are used as a regular functions 
we include them in our class when there is a logical connection to class functionality e.g is_work_day in Worker class   
"""


# sometimes it can be usefull to use @classmethod as a constructor for the class
# for example if information provided from somewhere and based on that information our classes are initialized
# e.g worker information is externally provided and has the following format "First-Last-Salary" and it constantly
# required to parse the string before creating a new instance of Worker


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

    @classmethod
    def from_string(cls, emp_str):
        # alternative constructor for emplyee data provided via string
        first, last, salary = emp_str.split('-')
        return cls(first, last, salary)
        # try:
        #     first, last, salary = emp_str.split('-')
        #     return cls(first, last, salary)
        # except Exception as e:
        #     print(e)
        #     return None

    # what about invalid parameters provided ? what if delimeter is wrong ?

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Worker):
    raise_amt = 1.10

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)  # there are multiple ways of doing that
        # Employee.__init__(first, last, salary) is considered less maintanable
        self.prog_lang = prog_lang


class Manager(Worker):
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


if __name__ == "__main__":
    sm = Developer("Sergei", "Miroshnikov", 200000, 'Python')
    print(sm.full_details())

# Region OLD
#
# emp_str1 = 'John-Doe-127000'
# emp_str2 = 'John-Smith-17000'
# emp_str3 = 'Asi-Koen-3500'
#
# jd = Worker.from_string(emp_str1)
# js = Worker.from_string(emp_str2)
# ak = Worker.from_string(emp_str3)
#
# print(ak.full_details())
# print(jd.full_details())
# print(js.full_details())
# print(Worker.is_workday(datetime.date.today()))
# """ Usage of static method in relation to our Worker project """
# date_to_check = datetime.date(2013, 1, 20)
# print(jd.is_workday(date_to_check))
# print(help(Developer))
# print(help(Worker))
# EndRegion
