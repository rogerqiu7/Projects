# Python Object-Oriented Programming
# allow us to logically group data and functions for ease of re-use 
# methods = function in a class

# create class, blueprint for instances
class Employee:

# CLASS VARIABLES, data shared among all employees
    num_of_emps = 0
    raise_amount = 1.04

# initialize method
    def __init__(self, first, last, pay):

# INSTANCE VARIABLES, different for each instance, keep arguements same as instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

# Employee.instead of self. because with raises, constant and overwritting, 
# this will never need to be different for any other instance.
        Employee.num_of_emps += 1

#instance methods
    def fullname(self):
        return "{} {}".format(self.first, self.last)

# self infront of raise amount, class variable needs to be accessed through class itself or instance
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# class method
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

# static if dont access this method anywhere in the method, 
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

import datetime
my_date = datetime.date(2016, 7, 10)


# will show 0 because before instantiated employees
print(Employee.num_of_emps)

# OBJECTS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! emp_1 and emp_2 passed as self
emp_1 = Employee("Roger", "Qiu", 65000)
emp_2 = Employee("Qiu", "Roger", 100000)

emp_str_1 = "Roger-Qiu-70000"
emp_str_2 = "Qiu-Roger-80000"

new_emp_1 = Employee.from_string(emp_str_1)

print(emp_1.email)

#need parenthesis at end because it is a method, not attribute
#if delete parenthesis, will print method, not return value
print(emp_1.fullname())

#does the same thing, this is longer, first print passes emp_1 as self 
print(Employee.fullname(emp_1))

#change raise amount through instance, changed to 1.05
emp_1.raise_amount = 1.05

#access raise amount through instance, actually accessing classes raise amount
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)

print(Employee.is_workday(my_date))


#inherited class, searches up the method resolution order
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):

# no need to copy from above, passes first, last and pay objects from employee
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


#another inherited class
class Manager(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())

dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("Test", "Employee", 60000, "Java")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

# see the method resolution order
print(help(Developer))

print(dev_1.email)

print(dev_1.pay)

dev_1.apply_raise()
# raise amount will be 10%, not 4%
print(dev_1.pay)

print(dev_1.prog_lang)

print(mgr_1.email)

mgr_1.add_emp(dev_2)

mgr_1.print_emps()

#tell us if an object is an instance of a class
print(isinstance(mgr_1, Manager)) 
print(isinstance(mgr_1, Developer))

#tell us if a class is a subclass of another
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))

print(1+2)
print("a" + "b")

#change first name
emp_1.first = "Jim"

# repr method now displays the code out
print(emp_1)
#represents the object for developers
print(repr(emp_1))

#readable representation for end user
str(emp_1)

#bracket test
def my_name(first, last):
    return "{} {} {}".format(first, first, last)

print(my_name("roger", "qiuuu"))