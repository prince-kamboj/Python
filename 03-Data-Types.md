# Python Data Types

## What are Data Types?

A data type defines the type of value a variable can store.

Examples:

```python
name = "Prince"
age = 22
height = 5.9
is_student = True
```

Python automatically determines the data type based on the assigned value.

---

# Why are Data Types Important?

Data types help Python understand:

- How much memory to allocate
- What operations can be performed
- How values should be stored and processed

Example:

```python
print(10 + 20)
```

Output:

```text
30
```

```python
print("10" + "20")
```

Output:

```text
1020
```

Same symbols, different data types, different behavior.

---

# Checking Data Types

Use the `type()` function.

```python
name = "Prince"

print(type(name))
```

Output:

```text
<class 'str'>
```

---

# Numeric Data Types

## 1. Integer (int)

Stores whole numbers.

```python
age = 22
marks = 95
temperature = -5
```

Examples:

```python
10
0
-50
100000
```

Check type:

```python
print(type(age))
```

Output:

```text
<class 'int'>
```

### Operations

```python
a = 20
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Output:

```text
30
10
200
2.0
2
0
10240000000000
```

---

## 2. Float (float)

Stores decimal numbers.

```python
price = 99.99
pi = 3.14159
temperature = 36.5
```

Examples:

```python
10.5
-8.75
0.0
```

Check type:

```python
print(type(price))
```

Output:

```text
<class 'float'>
```

### Operations

```python
a = 10.5
b = 2.5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Output:

```text
13.0
8.0
26.25
4.2
```

---

## 3. Complex Numbers (complex)

Stores imaginary numbers.

Syntax:

```python
number = 5 + 3j
```

Example:

```python
x = 3 + 4j

print(type(x))
```

Output:

```text
<class 'complex'>
```

Real part:

```python
print(x.real)
```

Output:

```text
3.0
```

Imaginary part:

```python
print(x.imag)
```

Output:

```text
4.0
```

---

# Text Data Type

## 4. String (str)

Stores text values.

Examples:

```python
name = "Prince"
city = 'Mumbai'
course = "Cybersecurity"
```

---

## String Operations

### Concatenation

```python
first = "Cyber"
second = "Security"

print(first + second)
```

Output:

```text
CyberSecurity
```

---

### Adding Space

```python
print(first + " " + second)
```

Output:

```text
Cyber Security
```

---

### Repetition

```python
print("Hi " * 3)
```

Output:

```text
Hi Hi Hi
```

---

### Length

```python
name = "Prince"

print(len(name))
```

Output:

```text
6
```

---

### Indexing

```python
name = "Prince"

print(name[0])
print(name[1])
```

Output:

```text
P
r
```

---

### Negative Indexing

```python
print(name[-1])
```

Output:

```text
e
```

---

### Slicing

```python
print(name[0:3])
```

Output:

```text
Pri
```

---

### Uppercase

```python
print(name.upper())
```

Output:

```text
PRINCE
```

---

### Lowercase

```python
print(name.lower())
```

Output:

```text
prince
```

---

### Replace

```python
text = "I love Java"

print(text.replace("Java", "Python"))
```

Output:

```text
I love Python
```

---

### Split

```python
text = "Linux,Python,Networking"

print(text.split(","))
```

Output:

```text
['Linux', 'Python', 'Networking']
```

---

# Boolean Data Type

## 5. Boolean (bool)

Stores only two values:

```text
True
False
```

Examples:

```python
is_logged_in = True
is_admin = False
```

Check type:

```python
print(type(is_admin))
```

Output:

```text
<class 'bool'>
```

---

## Boolean Operations

### AND

```python
print(True and True)
print(True and False)
```

Output:

```text
True
False
```

---

### OR

```python
print(True or False)
```

Output:

```text
True
```

---

### NOT

```python
print(not True)
```

Output:

```text
False
```

---

# Sequence Data Types

## 6. List (list)

Ordered and mutable collection.

```python
ports = [22, 80, 443, 8080]
```

Access:

```python
print(ports[0])
```

Output:

```text
22
```

Add item:

```python
ports.append(3306)
```

Remove item:

```python
ports.remove(80)
```

---

## 7. Tuple (tuple)

Ordered but immutable collection.

```python
coordinates = (10, 20)
```

Cannot modify:

```python
coordinates[0] = 5
```

Produces error.

---

## 8. Range (range)

Used for loops.

```python
numbers = range(5)

for x in numbers:
    print(x)
```

Output:

```text
0
1
2
3
4
```

---

# Set Data Type

## 9. Set (set)

Unordered collection of unique values.

```python
ports = {22, 80, 443}
```

Add value:

```python
ports.add(8080)
```

Remove value:

```python
ports.remove(22)
```

---

## Set Operations

### Union

```python
a = {1,2,3}
b = {3,4,5}

print(a | b)
```

Output:

```text
{1,2,3,4,5}
```

---

### Intersection

```python
print(a & b)
```

Output:

```text
{3}
```

---

### Difference

```python
print(a - b)
```

Output:

```text
{1,2}
```

---

# Mapping Data Type

## 10. Dictionary (dict)

Stores data in key-value pairs.

```python
student = {
    "name": "Prince",
    "age": 22,
    "course": "BCA"
}
```

Access value:

```python
print(student["name"])
```

Output:

```text
Prince
```

Add item:

```python
student["city"] = "Mumbai"
```

Update:

```python
student["age"] = 23
```

Delete:

```python
del student["course"]
```

---

# Special Data Type

## 11. NoneType

Represents absence of value.

```python
data = None

print(data)
```

Output:

```text
None
```

---

# Type Conversion

## Convert to Integer

```python
int("100")
```

---

## Convert to Float

```python
float("10")
```

---

## Convert to String

```python
str(100)
```

---

## Convert to List

```python
list("Python")
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

---

# Mutable vs Immutable

| Data Type | Mutable (n|y) |
|----------|---------|
| int | n |
| float | n |
| bool | n |
| str | n |
| tuple | n |
| list | y |
| set | y |
| dict | y |

---

# Data Types Used in Cybersecurity

## IP Address

```python
ip = "192.168.1.1"
```

Type:

```text
str
```

---

## Port Number

```python
port = 443
```

Type:

```text
int
```

---

## Open Ports

```python
ports = [22, 80, 443]
```

Type:

```text
list
```

---

## User Information

```python
user = {
    "username": "admin",
    "uid": 1000
}
```

Type:

```text
dict
```

---

# Key Takeaways

- Python supports multiple built-in data types.
- Every variable has a data type.
- Different data types support different operations.
- Understanding data types is essential before learning loops, functions, and object-oriented programming.
- Lists, dictionaries, and strings are heavily used in cybersecurity scripting.