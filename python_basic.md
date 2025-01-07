# Python Examples: Basic to Advanced

## **Basic Python**

### 1. Printing Output

```
print("Hello, World!")
```
Prints text to the console.

### 2. Variables and Data Types
```
name = "Alice"
age = 25
```
Stores data in variables with different types (string, integer).

### 3. Conditionals

```
if age > 18:
    print("Adult")
else:
    print("Minor")
```
Executes code based on conditions.

### 4. Loops

```
for i in range(5):
    print(i)
```
Loops through numbers from 0 to 4.

### 5. Functions

```
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
```
Defines and calls a function.

### 6. List Comprehension

```
squares = [x**2 for x in range(5)]
```
Creates a list by applying an operation to each element.

## **Intermediate Python**
### 1. File Handling

```
with open("example.txt", "w") as file:
    file.write("Hello, World!")
```
Writes data to a file.

### 2. Error Handling

```
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```
Handles errors gracefully.

### 3. Classes and Objects

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}."
alice = Person("Alice", 25)
print(alice.introduce())
```
Implements object-oriented programming with classes.

### 4. List Slicing

```
lst = [1, 2, 3, 4, 5]
print(lst[1:4])
```
Extracts a portion of a list.

### 5. Dictionary Operations

```
data = {"name": "Alice", "age": 25}
print(data.get("name"))
```
Works with key-value pairs.

## **Advanced Python**
###1. Lambda Functions

```
add = lambda x, y: x + y
print(add(5, 3))
```
Creates anonymous functions for simple operations.

### 2. Decorators

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
Extends the functionality of a function.

### 3. Generators

```
def count_up_to(n):
    for i in range(n):
        yield i
for num in count_up_to(5):
    print(num)
```
Generates values one at a time with yield.

### 4. Comprehensions with Conditions

```
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```
Creates lists with conditional logic.

### 5. Context Managers

```
with open("example.txt", "r") as file:
    content = file.read()
print(content)
```
Manages resources like file handling efficiently.

### 6. Multithreading

```
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
```
Executes tasks concurrently using threads.

### 7. Regular Expressions

```
import re
pattern = r"\d+"
result = re.findall(pattern, "There are 12 apples and 34 bananas.")
print(result)
```
Extracts patterns from strings using regex.

### 8. Working with JSON

```
import json
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
print(json_string)
```
Serializes Python objects into JSON format.

### 9. Itertools

```
from itertools import combinations
items = [1, 2, 3]
print(list(combinations(items, 2)))
```
Generates combinations or permutations of data.

### 10. Unit Testing

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
Tests code functionality systematically.
