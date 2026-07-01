# Python Variables

## What is a Variable?

A variable is a named storage location used to store data in memory.

Think of a variable as a container that stores information which can be used and modified throughout the program.

Example:

```python
name = "Prince"
age = 22
```

Here:

- `name` stores `"Prince"`
- `age` stores `22`

---

## Why Use Variables?

Variables allow programs to:

- Store information
- Reuse values
- Modify data
- Perform calculations
- Accept user input

Example:

```python
price = 100
quantity = 5

total = price * quantity

print(total)
```

Output:

```text
500
```

---

## Variable Assignment

Variables are assigned using the `=` operator.

Syntax:

```python
variable_name = value
```

Example:

```python
city = "Mumbai"
temperature = 32
```

---

## Multiple Variable Assignment

### Assign Multiple Variables

```python
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)
```

Output:

```text
10
20
30
```

---

### Assign Same Value to Multiple Variables

```python
a = b = c = 100

print(a)
print(b)
print(c)
```

Output:

```text
100
100
100
```

---

## Variable Naming Rules

### Valid Names

```python
name = "Prince"
age = 22
user_name = "admin"
student1 = "John"
_marks = 90
```

### Invalid Names

```python
1name = "Prince"
user-name = "admin"
class = "BCA"
```

Reasons:

- Cannot start with numbers.
- Cannot contain spaces.
- Cannot contain special symbols except `_`.
- Cannot use Python keywords.

---

## Naming Conventions

### Snake Case (Recommended)

```python
first_name = "Prince"
total_marks = 500
network_speed = 100
```

### Camel Case

```python
firstName = "Prince"
totalMarks = 500
```

### Pascal Case

```python
FirstName = "Prince"
```

---

## Variable Types

Python automatically determines variable types.

Example:

```python
name = "Prince"
age = 22
height = 5.9
is_student = True
```

---

## Checking Variable Type

Use `type()` function.

```python
name = "Prince"

print(type(name))
```

Output:

```text
<class 'str'>
```

Example:

```python
age = 22
print(type(age))

height = 5.9
print(type(height))

is_admin = True
print(type(is_admin))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

# Basic Data Types

## Integer (`int`)

Stores whole numbers.

```python
age = 22
marks = 95
```

Examples:

```python
10
-50
0
5000
```

---

## Float (`float`)

Stores decimal values.

```python
price = 99.99
temperature = 36.5
```

Examples:

```python
5.5
10.25
-8.2
```

---

## String (`str`)

Stores text data.

```python
name = "Prince"
city = 'Mumbai'
```

Examples:

```python
"Cybersecurity"
"Linux"
"Python"
```

---

## Boolean (`bool`)

Stores logical values.

```python
is_logged_in = True
is_admin = False
```

---

## None Type (`NoneType`)

Represents no value.

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

## Integer to Float

```python
age = 22

result = float(age)

print(result)
```

Output:

```text
22.0
```

---

## Float to Integer

```python
price = 99.99

result = int(price)

print(result)
```

Output:

```text
99
```

---

## Integer to String

```python
age = 22

result = str(age)

print(result)
```

Output:

```text
22
```

---

## String to Integer

```python
number = "100"

result = int(number)

print(result)
```

Output:

```text
100
```

---

# Variable Operations

## Addition

```python
a = 10
b = 20

print(a + b)
```

Output:

```text
30
```

---

## Subtraction

```python
print(a - b)
```

Output:

```text
-10
```

---

## Multiplication

```python
print(a * b)
```

Output:

```text
200
```

---

## Division

```python
print(a / b)
```

Output:

```text
0.5
```

---

## Floor Division

```python
print(a // b)
```

Output:

```text
0
```

---

## Modulus

```python
print(a % b)
```

Output:

```text
10
```

---

## Exponentiation

```python
print(a ** 2)
```

Output:

```text
100
```

---

# String Operations

## Concatenation

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

## Repetition

```python
print("Hi " * 3)
```

Output:

```text
Hi Hi Hi
```

---

# Comparison Operations

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

Output:

```text
False
True
False
True
False
True
```

---

# Logical Operations

## AND

```python
print(True and False)
```

Output:

```text
False
```

---

## OR

```python
print(True or False)
```

Output:

```text
True
```

---

## NOT

```python
print(not True)
```

Output:

```text
False
```

---

# Updating Variables

```python
count = 10

count = count + 1

print(count)
```

Output:

```text
11
```

Shortcut:

```python
count += 1
```

---

# Deleting Variables

```python
name = "Prince"

del name
```

---

# Memory Address of Variables

Use `id()`:

```python
x = 100

print(id(x))
```

Output:

```text
140732128
```

---

# Best Practices

Use meaningful names

```python
student_name = "Prince"
```

Avoid:

```python
x = "Prince"
```

---

Use snake_case

```python
network_speed = 100
```

---

Keep names descriptive

```python
failed_login_attempts = 5
```

---

# Variables in Cybersecurity Examples

## IP Address Storage

```python
ip_address = "192.168.1.1"
```

---

## Port Number

```python
port = 80
```

---

## Login Status

```python
is_authenticated = False
```

---

## Target Host

```python
target_host = "google.com"
```

---

# Key Takeaways

- Variables store data in memory.
- Python automatically determines data types.
- Variables can be updated and reused.
- Good naming conventions improve readability.
- Variables are the foundation of every Python program.