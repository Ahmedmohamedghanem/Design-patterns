#Design Patterns
#creational patterns
class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "triangle":
            return Triangle()
        else:
            raise ValueError("Invalid shape type")

# Define the Circle, Rectangle, and Triangle classes
class Circle:
    pass

class Rectangle:
    pass

class Triangle:
    pass

shape_factory = ShapeFactory()
circle = shape_factory.create_shape("circle")
rectangle = shape_factory.create_shape("rectangle")
triangle = shape_factory.create_shape("triangle")
#Structural patterns
class Pizza:
    def get_description(self):
        pass

    def get_cost(self):
        pass

class Margherita(Pizza):
    def get_description(self):
        return "Margherita"

    def get_cost(self):
        return 8.99

class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()

class ExtraCheese(PizzaDecorator):
    def get_description(self):
        return super().get_description() + ", Extra Cheese"

    def get_cost(self):
        return super().get_cost() + 1.99

margherita = Margherita()
margherita_with_extra_cheese = ExtraCheese(margherita)


#Behavioral patterns
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class Observer:
    def update(self):
        pass

class ConcreteObserver(Observer):
    def update(self):
        print("Update received")

subject = Subject()
observer = ConcreteObserver()
subject.attach(observer)
subject.notify()
###############################################################

# Model
#Architecture patterns
#MVC
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# View
class UserView:
    def display_user_details(self, username):
        print(f"Username: {username}")

# Controller
class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_user_details(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = self.model(username, password)
        self.view.display_user_details(user.username)  # Pass the username attribute
        ###########################################################
#solid principles
#single responsibility principle(srp)
# Usage
model = User
view = UserView()
controller = UserController(model, view)
controller.get_user_details()
class FileManager:

definit (self, filename): self.path Path(filename)

def read(self, encoding="utf-8"): return self.path.read_text(encoding)

def write(self, data, encoding="utf-8"): self.path.write_text(data, encoding)

def compress(self): with ZipFile(self.path.with_suffix(".zip"), mode-"w") as archive: archive.write(self.path)

def decompress(self): with ZipFile(self.path with suffix(".zip"), mode"r") as archive: archive.extractall()
##solve
class FileManager:

def _init_(self, filename): self.path Path(filename)

def read(self, encoding="utf-8"):

return self.path.read_text(encoding)

def write(self, data, encoding="utf-8"): self.path.write_text(data, encoding)

class ZipFileManager:

def _init(self, filename): self.path Path(filename)

def compress(self):

with ZipFile(self.path.with_suffix(".zip"), mode "w") as archive: archive.write(self.path)

def decompress(self):

with ZipFile(self.path.with_suffix(".zip"), mode "r") as archive:

archive.extractall()

#Open/Closed Principle (OCP)
class shape:

def _init_(self, shape_type, **kwargs): self.shape_type shape_type

if self.shape_type == "rectangle":

self.width = kwargs["width"] self.height kwargs["height"]

elif self.shape_type == "circle": self.radius = kwargs["radius"]

def calculate_area(self):

if self.shape_type == "rectangle": return self.width self.height

elif self.shape_type == "circle": return pi self.radius**2
##solve
class Shape(ABC)

def init(self, shape_type):

self.shape_type shape type

@abstractmethod

def calculate_area(self): pass

class Circle(Shape):

def_init_(self, radius): super()._init_("circle") self.radius = radius

def calculate_area(self):

return pi self.radius**2

class Rectangle(Shape):

def_init_(self, width, height):

super()_init__("rectangle")

self.width width

self.height height

def calculate_area(self):

return self.width

self height

class Square (Shape):

def _init_(self, side):

super().init("square")

self.side side

def calculate_area(self):

return self.side**2
###Liskov Substitution Principle (LSP)
class Shape(ABC): @abstractmethod

def calculate_area(self):

pass

class Rectangle(Shape):

def __init_(self, width, height):

self.width width

self.height height

def calculate_area(self):

return self.width self.height

class Square (Shape):

def _init_(self, side):

self.side side

def calculate_area(self):

return self.side ** 2
#####solve 
class Rectangle:

def _init__(self, width, height):

self.width = width self.height = height

def calculate_area(self): return self.width self.height
class Square (Rectangle):
    def _init__(self, side): super()._init_(side, side)
    def _setattr_(self, key, value): super().setattr_(key, value) if key in
    ("width", "height"): self._dict_ ["width"] = value self._dict_ ["height"] = value

##Interface Segregation Principle (ISP)
class Printer(ABC):

@abstractmethod

def print(self, document): pass

@abstractmethod

def fax(self, document): pass

@abstractmethod

def scan(self, document): pass

class OldPrinter (Printer):

def print(self, document):

print(f"Printing (document) in black and white...")

def fax(self, document):

raise NotImplementedError("Fax functionality not supported")

def scan(self, document):

raise NotImplementedError("Scan functionality not supported")

class ModernPrinter (Printer):

def print(self, document):

print(f"Printing (document) in color...")

def fax(self, document):

print(f"Faxing (document)...")

def scan(self, document): print("Scanning (document))
##solve
# class Printer(ABC):
@abstractmethod
def print(self, document):
pass
class Fax(ABC): @abstractmethod
def fax(self, document):
pass
class Scanner(ABC): @abstractmethod
def scan(self, document):
pass
class OldPrinter(Printer):
def print(self, document): print(f"Printing (document) in black and white...")
class NewPrinter (Printer, Fax, Scanner):
def print(self, document): print(f"Printing (document) in color...")
def fax(self, document): print(f Faxing (document)...")
def scan(self, document): print(f"Scanning (document)...)

###Dependency inversion principle
class FrontEnd:

def __init_(self, back_end):

self.back_end = back_end

def display_data(self):

data = self.back_end.get_data_from_database() print("Display data:", data)

class BackEnd:

def get_data_from_database(self):

return "Data from the database"
###solve
class Front End:

def init(self, data_source): self.data_source = data_source

def display_data(self): data self.data_source.get_data() print("Display data:", data)

class DataSource (ABC): @abstractmethod

def get_data(self): pass

class Database (DataSource):

def get_data(self):

return "Data from the database"

class API (DataSource):

def get_data(self): return "Data from the API"
##########################################################################################

#Test Driven Development 
###test_calculator.py in the test directory with the following contents.

import unittest
class IddInPythonExample(unittest.TestCase):
rectory and import it:
def test calculator_add method returns_correct_result(self):
calc Calculator()
result calc.add(2,2) self.assertEqual(4, result)
class Calculator(object):

def add(self, x, y):

return x+y
#output
$ nosetests test_calculator.py
............
----------------------------

Ran 1 test in 0.0005
OK

#####################
#assertRaises
import unittest
from app.calculator import Calculator
class TddInPythonExample(unittest.TestCase):
def setup(self):
self.calc calculator()
def test_calculator_add_method_returns_correct_result(self): result = self.calc.add(2, 2)

self.assertEqual(4, result)

def test_calculator_returns_error_message_if_both_args_not_numbers(self): self.assertRaises (ValueError, self.calc.add, 'two', 'three')

if_name = '_main_': unittest.main()
########
 import unittest

from app.calculator import Calculator

class TddInPythonExample(unittest. TestCase):


def setup(self):

self.calc Calculator()

def test calculator_add_method_returns_correct_result(self):

result self.calc.add(2, 2) self.assertEqual(4, result)

def test calculator_returns_error_message_if_both_args_not_numbers(self): self.assertRaises (ValueError, self.calc.add, 'two', 'three')

def test calculator_returns_error message_if_x_arg_not_number(self): self.assertRaises (ValueError, self.calc.add, 'two', 3)

def test calculator_returns_error_message_if_y_arg_not_number(self): self.assertRaises (ValueError, self.calc.add, 2, 'three')

if__name__"" '__main__':
unittest.main()
 nosetests test_calculator.py
 .........
 ----------------------------------
Ran 4 test in 0.001s
OK
