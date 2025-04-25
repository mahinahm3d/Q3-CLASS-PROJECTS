#01-Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")

# Usage
s = Student("Alice", 95)
s.display()


#02-Using cls
class Counter:
    count = 0
    
    def __init__(self):
        Counter.increment_count()
    
    @classmethod
    def increment_count(cls):
        cls.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

# Usage
c1 = Counter()
c2 = Counter()
print(Counter.get_count())  # Output: 2


#03-Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} car started")

# Usage
my_car = Car("Toyota")
print(my_car.brand)  # Public variable
my_car.start()       # Public method


#04-Class Variables and Class Methods
class Bank:
    bank_name = "First National Bank"
    
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

# Usage
b1 = Bank()
b2 = Bank()
print(b1.bank_name)  # Output: First National Bank

Bank.change_bank_name("Global Bank")
print(b2.bank_name)  # Output: Global Bank


#05-Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Usage
print(MathUtils.add(5, 3))  # Output: 8


#06-Constructors and Destructors
class Logger:
    def __init__(self, name):
        self.name = name
        print(f"Logger {name} created")
    
    def __del__(self):
        print(f"Logger {self.name} destroyed")

# Usage
logger = Logger("AppLogger")
del logger  # Destructor called


#07-Access Modifiers
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn         # Private

# Usage
emp = Employee("John", 50000, "123-45-6789")
print(emp.name)        # Works
print(emp._salary)     # Works but convention says "don't do this"
# print(emp.__ssn)     # Raises AttributeError
print(emp._Employee__ssn)  # Name mangling (not recommended)


#08-The super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Usage
teacher = Teacher("Mrs. Smith", "Math")
print(f"{teacher.name} teaches {teacher.subject}")


#09-Abstract Classes and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Usage
rect = Rectangle(5, 10)
print(rect.area())  # Output: 50


#010- Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")

# Usage
dog = Dog("Buddy", "Golden Retriever")
dog.bark()


#011-Class Methords
class Book:
    total_books = 0
    
    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books

# Usage
b1 = Book("Python 101")
b2 = Book("Advanced Python")
print(Book.get_total_books())  # Output: 2


#012-Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Usage
print(TemperatureConverter.celsius_to_fahrenheit(30))  # Output: 86.0


#013-Composition
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def start(self):
        self.engine.start()
        print("Car started")

# Usage
car = Car()
car.start()


#014-Aggregation
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees if employees else []
    
    def add_employee(self, employee):
        self.employees.append(employee)

# Usage
emp1 = Employee("John")
emp2 = Employee("Jane")
dept = Department("IT")
dept.add_employee(emp1)
dept.add_employee(emp2)

for emp in dept.employees:
    print(emp.name)


#015-Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# Usage
d = D()
d.show()  # Output: B (due to MRO)
print(D.mro())  # Shows method resolution order


#016-Function Decorators
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# Usage
say_hello()


#017-Class Decorators
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    pass

# Usage
p = Person()
print(p.greet())


#018-Property Decorators
class Product:
    def __init__(self, price):
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @price.deleter
    def price(self):
        print("Price deleted")
        del self._price

# Usage
p = Product(100)
print(p.price)  # Get
p.price = 150   # Set
# p.price = -10 # Raises ValueError
del p.price     # Delete


#019-callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

# Usage
double = Multiplier(2)
print(callable(double))  # Output: True
print(double(5))         # Output: 10


#020-Creating a Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    return "Valid age"

# Usage
try:
    print(check_age(20))  # Works
    print(check_age(15))  # Raises exception
except InvalidAgeError as e:
    print(f"Error: {e}")


#021-Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1

# Usage
for num in Countdown(5):
    print(num)  # Output: 5, 4, 3, 2, 1