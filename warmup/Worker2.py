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

    "alternative constructor for emplyee data provided via string "

    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split('-')
        return Worker(first, last, salary)


if __name__ == "__main__":
    emp_str1 = 'John-Doe-127000'
    emp_str2 = 'John-Smith-17000'
    emp_str3 = 'Asi-Koen-3500'

    jd = Worker.from_string(emp_str1)
    js = Worker.from_string(emp_str2)
    ak = Worker.from_string(emp_str3)

    print(ak.full_details())
    print(jd.full_details())
    print(js.full_details())
