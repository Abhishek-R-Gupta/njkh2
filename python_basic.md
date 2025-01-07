# Python Concepts: From Basic to Advanced

## 1. **Operators**

### Arithmetic Operators

```
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
```
Performs basic arithmetic operations.

### Comparison Operators

```
a = 10
b = 5
print(a > b)   # Greater than
print(a == b)  # Equal to
print(a != b)  # Not equal to
```
Compares values to return a boolean.

### Logical Operators

```
x = True
y = False
print(x and y)  # Logical AND
print(x or y)   # Logical OR
print(not x)    # Logical NOT
```
Used to perform logical operations.

## 2. Conditions
### Basic If-Else Statement

```
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")
```
Checks if a condition is true or false.

### Elif Example

```
age = 15
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```
Handles multiple conditions.

## 3. Loops
### For Loop

```
for i in range(5):
    print(i)
```
Loops through a sequence or range.

### While Loop

```
i = 0
while i < 5:
    print(i)
    i += 1
```
Executes code while a condition is true.

### Break and Continue

```
for i in range(5):
    if i == 3:
        break  # Exits the loop
    print(i)
    
for i in range(5):
    if i == 3:
        continue  # Skips this iteration
    print(i)
```
Control flow to break or skip iterations.

## 4. Lists
### Creating and Accessing Lists

```
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Accesses the first element
```
Stores multiple items in an ordered sequence.

### List Methods

```
fruits.append("orange")
fruits.remove("banana")
print(fruits)
```
Common operations like adding/removing items.

### List Slicing

```
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # Extracts a sublist
```
Access a range of elements in a list.

## 5. Tuples
### Creating and Accessing Tuples

```
coordinates = (10, 20)
print(coordinates[0])  # Accesses first element
```
Stores multiple items in an ordered, immutable sequence.

### Tuple Unpacking

```
x, y = coordinates
print(x, y)
```
Assigns elements of a tuple to variables.

## 6. Sets
### Creating and Accessing Sets

```
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
```
Unordered collection with no duplicates.

### Set Operations

```
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)  # Intersection
print(set1 | set2)  # Union
```
Set operations like intersection and union.

## 7. Dictionaries
### Creating and Accessing Dictionaries

```
person = {"name": "Alice", "age": 25}
print(person["name"])
```
Stores data in key-value pairs.

### Dictionary Methods

```
person["city"] = "New York"  # Adds new key-value pair
del person["age"]  # Removes key-value pair
print(person)
```
Manipulates dictionary entries.

## 8. Functions
### Defining Functions

```
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
```
Defines a function that performs a specific task.

### Default Arguments

```
def greet(name, age=25):
    return f"Hello, {name}. You are {age} years old."
print(greet("Bob"))
```
Defines functions with default argument values.

### Lambda Functions

```
add = lambda x, y: x + y
print(add(5, 3))
```
Creates anonymous functions for simple operations.

## 9. Comprehensions
### List Comprehension

```
squares = [x**2 for x in range(5)]
print(squares)
```
Generates a new list by applying an operation to each element.

### Dictionary Comprehension

```
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)
```
Creates dictionaries using a comprehension.

### Set Comprehension

```
unique_numbers = {x for x in range(5)}
print(unique_numbers)
```
Creates sets using comprehension.

## 10. Additional Important Topics
### Exception Handling (Try-Except)

```
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
```
Catches and handles errors to prevent program crashes.

### Working with Files

```
with open("example.txt", "w") as file:
    file.write("Hello, World!")
```
Reads/writes data to/from files.

### Classes and Objects

```
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.name)
```
Defines and instantiates a class.

### Iterators and Generators

```
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)
```
Generates values one at a time with yield.

### Regular Expressions

```
import re
pattern = r"\d+"
text = "There are 12 apples and 34 bananas."
matches = re.findall(pattern, text)
print(matches)
```
Extracts patterns from strings using regular expressions.

## 11. Advanced Python
### Decorators

```
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
```
Enhances the functionality of a function without modifying it.

### Context Managers

```
with open("file.txt", "r") as file:
    content = file.read()
print(content)
```
Manages resources automatically (e.g., file handling).

### Multithreading

```
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
```
Executes multiple tasks simultaneously.

### Unit Testing

```
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```
Tests the correctness of code with assertions.
