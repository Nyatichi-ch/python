# Defining a class

class fruit:
    def __init__(self, type, flavor, color):
        self.type = type    # Instance variable
        self.flavor = flavor    # Instance variable
        self.color = color    # Instance variable
    
# methods
    def taste(self):
        return f"The {self.type} is {self.flavor}."
    def appearance(self):
        return f"The {self.type} is {self.color} in color."

# Creating objects with unique attributes
mango = fruit("Tropical", "sweet", "yellow")
avacado = fruit("Hass", "creamy", "green")

print(mango.flavor)  # Output: sweet
print(avacado.type)  # Output: Hass

# add inheritance
class citrus(fruit):  # Inheriting from fruit class
    def __init__(self, type, flavor, color, acidity):
        super().__init__(type, flavor, color)  # Calling the parent class constructor
        self.acidity = acidity  # New attribute for citrus class
        self.category = "Citrus"  # New attribute for citrus class

# explore polymorphism
def describe(self):
        return f"{self.type} is a {self.category} fruit that is {self.flavor} and has a {self.color} color."
def health_benefits(self):
        return f"{self.type} is rich in Vitamin C and helps boost immunity."
def acidity_level(self):
        return f"{self.type} has an acidity level of {self.acidity}."
def vitamin_content(self):
        return f"{self.type} has a vitamin C content that is {self.vitamin_c_content}."
    
# explore encapsulation
def get_acidity(self):
        return self.acidity
def set_acidity(self, acidity):
        self.acidity = acidity
def get_vitamin_c_content(self):
        return self.vitamin_c_content
def set_vitamin_c_content(self, vitamin_c_content):
        self.vitamin_c_content = vitamin_c_content

orange = citrus("Orange", "tangy", "orange", "medium")
lemon = citrus("Lemon", "sour", "yellow", "high")

print(orange.taste())  # Output: The Orange is tangy.
print(lemon.appearance())  # Output: The Lemon is yellow in color.


# a program that includes vehicles with the same action

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  def move(self):
    print("Driving!")

class Boat(Vehicle):
  def move(self):
    print("Sailing!")

class Plane(Vehicle):
  def move(self):
    print("Flying!")

vehicles = [Car("Toyota", "Corolla"), Boat("Yamaha", "242X"), Plane("Boeing", "747")]
for v in vehicles:
  v.move()

    