# Python Operators

## Introduction

Operators are special symbols or keywords in Python that perform operations on variables and values.

They are used to perform tasks such as:

- Mathematical calculations
- Comparing values
- Making logical decisions
- Assigning values
- Checking membership
- Comparing object identity
- Performing bit-level operations

Example:

```python
a = 10
b = 5

print(a + b)
```

Output:

```text
15
```

---

# Types of Operators in Python

Python provides the following categories of operators:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators

---

# 1. Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 2` |
| `-` | Subtraction | `5 - 2` |
| `*` | Multiplication | `5 * 2` |
| `/` | Division | `5 / 2` |
| `//` | Floor Division | `5 // 2` |
| `%` | Modulus | `5 % 2` |
| `**` | Exponent | `5 ** 2` |

### Addition

```python
a = 10
b = 20

print(a + b)
```

Output

```text
30
```

---

### Subtraction

```python
print(20 - 5)
```

Output

```text
15
```

---

### Multiplication

```python
print(6 * 7)
```

Output

```text
42
```

---

### Division

```python
print(10 / 3)
```

Output

```text
3.3333333333333335
```

Division always returns a float.

---

### Floor Division

```python
print(10 // 3)
```

Output

```text
3
```

Removes the decimal part.

---

### Modulus

```python
print(10 % 3)
```

Output

```text
1
```

Returns the remainder.

Common uses:

- Check even or odd numbers
- Cyclic operations

---

### Exponent

```python
print(2 ** 5)
```

Output

```text
32
```

---

# Operator Precedence

Python follows the order of operations.

1. Parentheses `()`
2. Exponent `**`
3. Multiplication, Division, Floor Division, Modulus
4. Addition, Subtraction

Example

```python
print(2 + 3 * 4)
```

Output

```text
14
```

---

# 2. Assignment Operators

Assignment operators assign values to variables.

| Operator | Example | Equivalent |
|----------|---------|------------|
| `=` | `x = 5` | Assign value |
| `+=` | `x += 2` | `x = x + 2` |
| `-=` | `x -= 2` | `x = x - 2` |
| `*=` | `x *= 2` | `x = x * 2` |
| `/=` | `x /= 2` | `x = x / 2` |
| `//=` | `x //= 2` | Floor divide assignment |
| `%=` | `x %= 2` | Modulus assignment |
| `**=` | `x **= 2` | Exponent assignment |

Example

```python
x = 10

x += 5

print(x)
```

Output

```text
15
```

---

# 3. Comparison Operators

Comparison operators compare two values.

They return either:

```python
True
```

or

```python
False
```

| Operator | Meaning |
|----------|---------|
| `==` | Equal |
| `!=` | Not Equal |
| `>` | Greater Than |
| `<` | Less Than |
| `>=` | Greater Than or Equal |
| `<=` | Less Than or Equal |

Example

```python
print(10 > 5)
```

Output

```text
True
```

---

Example

```python
print(10 == 5)
```

Output

```text
False
```

---

# 4. Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning |
|----------|---------|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses the result |

---

### AND

```python
age = 20

print(age >= 18 and age <= 30)
```

Output

```text
True
```

---

### OR

```python
print(False or True)
```

Output

```text
True
```

---

### NOT

```python
print(not True)
```

Output

```text
False
```

---

# Truth Table

## AND

| A | B | Result |
|---|---|--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

## OR

| A | B | Result |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## NOT

| A | Result |
|---|--------|
| True | False |
| False | True |

---

# 5. Identity Operators

Identity operators check whether two variables refer to the same object in memory.

| Operator | Meaning |
|----------|---------|
| `is` | Same object |
| `is not` | Different object |

Example

```python
a = [1, 2]
b = a

print(a is b)
```

Output

```text
True
```

---

Example

```python
a = [1, 2]
b = [1, 2]

print(a is b)
```

Output

```text
False
```

Although the values are equal, they are different objects.

---

# 6. Membership Operators

Membership operators check whether a value exists inside a sequence.

| Operator | Meaning |
|----------|---------|
| `in` | Value exists |
| `not in` | Value does not exist |

Example

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

Output

```text
True
```

---

Example

```python
print(100 not in numbers)
```

Output

```text
True
```

---

# 7. Bitwise Operators

Bitwise operators work directly with binary numbers.

| Operator | Description |
|----------|-------------|
| `&` | AND |
| `|` | OR |
| `^` | XOR |
| `~` | NOT |
| `<<` | Left Shift |
| `>>` | Right Shift |

Example

```python
print(5 & 3)
```

Output

```text
1
```

Binary:

```text
5 = 101
3 = 011

AND

001
```

---

# Operator Precedence (Highest to Lowest)

| Priority | Operator |
|----------|----------|
| 1 | `()` |
| 2 | `**` |
| 3 | `+x`, `-x`, `~x` |
| 4 | `*`, `/`, `//`, `%` |
| 5 | `+`, `-` |
| 6 | `<<`, `>>` |
| 7 | `&` |
| 8 | `^` |
| 9 | `|` |
| 10 | Comparison Operators |
| 11 | `not` |
| 12 | `and` |
| 13 | `or` |

---

# Common Mistakes

### Using `=` instead of `==`

Incorrect

```python
if a = 10:
```

Correct

```python
if a == 10:
```

---

### Confusing `is` and `==`

```python
a = [1, 2]
b = [1, 2]

print(a == b)
```

Output

```text
True
```

```python
print(a is b)
```

Output

```text
False
```

- `==` compares values.
- `is` compares object identity.

---

### Division Returns Float

```python
print(10 / 2)
```

Output

```text
5.0
```

Use `//` for integer division.

---

# Practice Examples

```python
a = 12
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

print(a > b)
print(a == b)
print(a != b)

print(a > 10 and b < 10)
print(a > 20 or b < 10)

numbers = [1, 2, 3, 4]

print(3 in numbers)
print(10 not in numbers)
```

---

# Best Practices

- Use parentheses to improve readability.
- Use `==` for value comparison.
- Use `is` only when checking object identity.
- Prefer meaningful variable names.
- Understand operator precedence to avoid unexpected results.

---

# Summary

- Operators perform actions on values and variables.
- Python has seven main categories of operators.
- Arithmetic operators handle calculations.
- Comparison operators return Boolean values.
- Logical operators combine conditions.
- Assignment operators update variable values.
- Identity operators compare object identity.
- Membership operators check if a value exists in a sequence.
- Bitwise operators manipulate binary data.

---

# Key Takeaways

- Learn the difference between `=` and `==`.
- Understand when to use `is` versus `==`.
- Remember operator precedence to write correct expressions.
- Practice using different operators to build confidence in writing Python programs.