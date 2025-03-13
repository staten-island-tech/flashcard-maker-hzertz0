# Lesson: Classes in Python

## Introduction to Classes
A **class** in Python is a blueprint for creating objects. It allows us to group data and behavior together. Classes help in organizing code, making it more reusable and scalable.

### Defining a Class
A class is defined using the `class` keyword. It typically contains attributes (variables) and methods (functions that operate on the attributes).

```python
import json

class Car:
    def __init__(self, make, model, year, image=None):
        self.make = make
        self.model = model
        self.year = year
        self.image = image
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
```

### Instantiating a Class and Saving to JSON
To create an object (an instance of a class), we call the class like a function, passing the required arguments.

```python
my_car = Car("Toyota", "Camry", 2023, "camry_image.jpg")
print(my_car.display_info())  # Output: 2023 Toyota Camry
```

To store multiple car instances into a JSON file:

```python
cars = [
    Car("Toyota", "Camry", 2023, "camry_image.jpg"),
    Car("Honda", "Civic", 2022, "civic_image.jpg"),
    Car("Ford", "Mustang", 2021, "mustang_image.jpg")
]

# Convert objects to dictionaries
cars_data = [car.to_dict() for car in cars]

# Save to a JSON file
with open("cars.json", "w") as file:
    json.dump(cars_data, file, indent=4)
```

### Appending New Cars to JSON File
To add more cars to the existing JSON file:

```python
new_car = Car("Chevrolet", "Malibu", 2024, "malibu_image.jpg")

# Load existing data
try:
    with open("cars.json", "r") as file:
        cars_data = json.load(file)
except FileNotFoundError:
    cars_data = []

# Append new car
cars_data.append(new_car.to_dict())

# Save updated data back to file
with open("cars.json", "w") as file:
    json.dump(cars_data, file, indent=4)
```

---

## Using a Class as a Function Container
Sometimes, we create classes that are meant to store related functions rather than instances with attributes. Such classes are typically implemented using `@staticmethod` or `@classmethod` decorators.

### Example: Math Utilities Class
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
```

### Using the Function Container Class
```python
print(MathUtils.add(5, 3))      # Output: 8
print(MathUtils.subtract(10, 4))  # Output: 6
print(MathUtils.multiply(2, 3))   # Output: 6
print(MathUtils.divide(9, 3))     # Output: 3.0
```

---

## Key Takeaways
1. **Classes group related data and behavior.**
2. **Instance attributes** are stored in `self` and defined in `__init__`.
3. **Methods** allow instances to interact with their attributes.
4. **Static methods** allow grouping of functions without requiring instance attributes.
5. **Classes make code more structured and reusable.**
6. **Instances can be serialized and stored in a JSON file for future use.**
7. **Appending new car instances to an existing JSON file ensures persistent storage without overwriting old data.**