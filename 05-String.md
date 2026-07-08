# Strings in Python 

## Introduction

A **string** is one of the most commonly used data types in Python. It represents a sequence of characters enclosed within quotation marks.

A string can contain:

- Letters
- Numbers
- Symbols
- Spaces
- Special characters
- Unicode characters

Strings are used to store and manipulate textual data such as names, addresses, messages, passwords, file paths, URLs, and more.

Examples:

```python
name = "Prince"
course = 'Python'
message = "Hello, World!"
password = "P@ssw0rd123"
```

---

# Characteristics of Strings

- Ordered sequence of characters.
- Immutable (cannot be modified after creation).
- Supports indexing and slicing.
- Can contain duplicate characters.
- Can store Unicode characters.
- Can be created using single, double, or triple quotes.

---

# Creating Strings

Python provides several ways to create strings.

## Single Quotes

```python
language = 'Python'

print(language)
```

Output

```text
Python
```

---

## Double Quotes

```python
language = "Python"

print(language)
```

Output

```text
Python
```

---

## Triple Quotes

Triple quotes are used for multi-line strings.

```python
message = """Welcome to Python.
This is a multi-line string.
Have a great day!"""

print(message)
```

Output

```text
Welcome to Python.
This is a multi-line string.
Have a great day!
```

---

# String Constructor

Strings can also be created using the `str()` constructor.

```python
number = 100

text = str(number)

print(text)
print(type(text))
```

Output

```text
100
<class 'str'>
```

---

# Accessing Characters (Indexing)

Each character in a string has an index.

Python uses **zero-based indexing**, meaning the first character is at index `0`.

Example:

```python
word = "Python"
```

| Character | P | y | t | h | o | n |
|-----------|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 |

---

## Access First Character

```python
word = "Python"

print(word[0])
```

Output

```text
P
```

---

## Access Third Character

```python
print(word[2])
```

Output

```text
t
```

---

## Access Last Character

```python
print(word[5])
```

Output

```text
n
```

---

# Negative Indexing

Python also supports negative indexing.

Negative indexes start from the end of the string.

| Character | P | y | t | h | o | n |
|-----------|---|---|---|---|---|---|
| Negative Index | -6 | -5 | -4 | -3 | -2 | -1 |

Example

```python
word = "Python"

print(word[-1])
```

Output

```text
n
```

---

```python
print(word[-3])
```

Output

```text
h
```

---

# String Slicing

Slicing allows you to extract a portion of a string.

Syntax

```python
string[start : stop : step]
```

Where:

- `start` → Starting index (included)
- `stop` → Ending index (excluded)
- `step` → Number of positions to move

---

## Basic Slicing

```python
word = "CyberSecurity"

print(word[0:5])
```

Output

```text
Cyber
```

---

```python
print(word[5:13])
```

Output

```text
Security
```

---

## Omitting Start

```python
print(word[:5])
```

Output

```text
Cyber
```

---

## Omitting Stop

```python
print(word[5:])
```

Output

```text
Security
```

---

## Copy Entire String

```python
print(word[:])
```

Output

```text
CyberSecurity
```

---

## Using Step

```python
print(word[::2])
```

Output

```text
CbrScrt
```

Every second character is selected.

---

## Reverse a String

```python
print(word[::-1])
```

Output

```text
ytiruceSrebyC
```

---

# String Immutability

Strings in Python are **immutable**.

This means you cannot change individual characters after the string is created.

Incorrect

```python
text = "Python"

text[0] = "J"
```

Output

```text
TypeError
```

---

Correct

```python
text = "Python"

text = "J" + text[1:]

print(text)
```

Output

```text
Jython
```

---

# Escape Characters

Escape characters allow special characters to be included inside strings.

| Escape Sequence | Meaning |
|----------------|---------|
| `\'` | Single Quote |
| `\"` | Double Quote |
| `\\` | Backslash |
| `\n` | New Line |
| `\t` | Horizontal Tab |
| `\r` | Carriage Return |
| `\b` | Backspace |

---

Example

```python
print("Hello\nWorld")
```

Output

```text
Hello
World
```

---

Example

```python
print("Python\tProgramming")
```

Output

```text
Python    Programming
```

---

# Raw Strings

A raw string ignores escape characters.

Prefix the string with `r`.

```python
path = r"C:\Users\Prince\Documents"

print(path)
```

Output

```text
C:\Users\Prince\Documents
```

Raw strings are commonly used for:

- Windows file paths
- Regular expressions

---

# String Concatenation

Concatenation means joining two or more strings.

Using `+`

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

Output

```text
Hello World
```

---

Using `+=`

```python
text = "Python"

text += " Programming"

print(text)
```

Output

```text
Python Programming
```

---

# String Repetition

The `*` operator repeats a string.

```python
print("Hi " * 3)
```

Output

```text
Hi Hi Hi
```

---

# Membership Operators

Check whether a substring exists.

Using `in`

```python
text = "Python Programming"

print("Python" in text)
```

Output

```text
True
```

---

Using `not in`

```python
print("Java" not in text)
```

Output

```text
True
```

---

# Iterating Through a String

Using a `for` loop

```python
text = "Python"

for letter in text:
    print(letter)
```

Output

```text
P
y
t
h
o
n
```

---

# Useful Built-in Functions

## len()

Returns the number of characters.

```python
text = "Python"

print(len(text))
```

Output

```text
6
```

---

## max()

Returns the character with the highest Unicode value.

```python
print(max("Python"))
```

Output

```text
y
```

---

## min()

Returns the character with the smallest Unicode value.

```python
print(min("Python"))
```

Output

```text
P
```

---

## sorted()

Returns a sorted list of characters.

```python
print(sorted("Python"))
```

Output

```python
['P', 'h', 'n', 'o', 't', 'y']
```

---

## ord()

Returns the Unicode value of a character.

```python
print(ord("A"))
```

Output

```text
65
```

---

## chr()

Returns the character for a Unicode value.

```python
print(chr(65))
```

Output

```text
A
```

---

# Common Mistakes

### Using Invalid Index

```python
text = "Python"

print(text[20])
```

Output

```text
IndexError
```

---

### Forgetting Strings are Immutable

```python
text[0] = "J"
```

This raises a `TypeError`.

Create a new string instead.

---

### Mixing Strings and Numbers

Incorrect

```python
age = 20

print("Age: " + age)
```

Correct

```python
age = 20

print("Age:", age)
```

Or

```python
print("Age: " + str(age))
```

---


# String Methods in Python 


> **Note:** Most string methods return a new string. If you want to keep the changes, assign the result back to a variable.

```python
text = "python"
text = text.upper()

print(text)
```

Output

```text
PYTHON
```

---

# Changing Letter Case

## upper()

Converts all characters to uppercase.

### Syntax

```python
string.upper()
```

Example

```python
text = "python programming"

print(text.upper())
```

Output

```text
PYTHON PROGRAMMING
```

---

## lower()

Converts all characters to lowercase.

```python
text = "PYTHON"

print(text.lower())
```

Output

```text
python
```

---

## capitalize()

Capitalizes only the first character.

```python
text = "python programming"

print(text.capitalize())
```

Output

```text
Python programming
```

---

## title()

Capitalizes the first letter of every word.

```python
text = "python programming language"

print(text.title())
```

Output

```text
Python Programming Language
```

---

## swapcase()

Converts uppercase letters to lowercase and vice versa.

```python
text = "Python"

print(text.swapcase())
```

Output

```text
pYTHON
```

---

## casefold()

Similar to `lower()`, but more aggressive for Unicode text.

```python
text = "HELLO"

print(text.casefold())
```

Output

```text
hello
```

---

# Removing Spaces and Characters

## strip()

Removes spaces from both ends.

```python
text = "   Python   "

print(text.strip())
```

Output

```text
Python
```

---

## lstrip()

Removes spaces from the left.

```python
text = "   Python"

print(text.lstrip())
```

Output

```text
Python
```

---

## rstrip()

Removes spaces from the right.

```python
text = "Python   "

print(text.rstrip())
```

Output

```text
Python
```

---

## remove specific characters

```python
text = "***Python***"

print(text.strip("*"))
```

Output

```text
Python
```

---

# Searching Methods

## find()

Returns the first index of a substring.

Returns **-1** if not found.

```python
text = "Python Programming"

print(text.find("Program"))
```

Output

```text
7
```

---

## rfind()

Searches from the right side.

```python
text = "one two one"

print(text.rfind("one"))
```

Output

```text
8
```

---

## index()

Works like `find()` but raises an error if the substring does not exist.

```python
text = "Python"

print(text.index("t"))
```

Output

```text
2
```

---

## rindex()

Searches from the right and raises an error if not found.

---

## count()

Counts occurrences of a substring.

```python
text = "banana"

print(text.count("a"))
```

Output

```text
3
```

---

# Replace Method

## replace()

Replaces one substring with another.

```python
text = "I like Java"

print(text.replace("Java", "Python"))
```

Output

```text
I like Python
```

---

Limit replacements

```python
text = "apple apple apple"

print(text.replace("apple", "orange", 2))
```

Output

```text
orange orange apple
```

---

# Splitting Strings

## split()

Splits a string into a list.

```python
text = "Python Java C++"

print(text.split())
```

Output

```python
['Python', 'Java', 'C++']
```

---

Split using a separator.

```python
text = "A,B,C,D"

print(text.split(","))
```

Output

```python
['A', 'B', 'C', 'D']
```

---

Limit splits.

```python
text = "A,B,C,D"

print(text.split(",", 2))
```

Output

```python
['A', 'B', 'C,D']
```

---

## rsplit()

Splits from the right.

```python
text = "one-two-three"

print(text.rsplit("-", 1))
```

Output

```python
['one-two', 'three']
```

---

## splitlines()

Splits a multi-line string.

```python
text = "One\nTwo\nThree"

print(text.splitlines())
```

Output

```python
['One', 'Two', 'Three']
```

---

# Joining Strings

## join()

Joins elements of an iterable into a string.

```python
languages = ["Python", "Java", "C"]

print(", ".join(languages))
```

Output

```text
Python, Java, C
```

---

# Starts and Ends

## startswith()

Checks whether a string starts with a substring.

```python
text = "Python"

print(text.startswith("Py"))
```

Output

```text
True
```

---

## endswith()

Checks whether a string ends with a substring.

```python
text = "notes.md"

print(text.endswith(".md"))
```

Output

```text
True
```

---

# Validation Methods

## isalpha()

Returns True if all characters are alphabetic.

```python
print("Python".isalpha())
```

Output

```text
True
```

---

## isdigit()

Checks whether all characters are digits.

```python
print("12345".isdigit())
```

Output

```text
True
```

---

## isnumeric()

Checks whether all characters are numeric.

```python
print("123".isnumeric())
```

Output

```text
True
```

---

## isdecimal()

Checks whether all characters are decimal numbers.

```python
print("123".isdecimal())
```

Output

```text
True
```

---

## isalnum()

Checks whether all characters are letters or numbers.

```python
print("Python3".isalnum())
```

Output

```text
True
```

---

## isspace()

Checks whether a string contains only whitespace.

```python
print("   ".isspace())
```

Output

```text
True
```

---

## islower()

```python
print("python".islower())
```

Output

```text
True
```

---

## isupper()

```python
print("PYTHON".isupper())
```

Output

```text
True
```

---

## istitle()

```python
print("Python Programming".istitle())
```

Output

```text
True
```

---

# Alignment Methods

## center()

Centers the string.

```python
text = "Python"

print(text.center(20, "-"))
```

Output

```text
-------Python-------
```

---

## ljust()

Aligns text to the left.

```python
print("Python".ljust(15, "."))
```

Output

```text
Python.........
```

---

## rjust()

Aligns text to the right.

```python
print("Python".rjust(15, "."))
```

Output

```text
.........Python
```

---

## zfill()

Pads a string with leading zeros.

```python
print("25".zfill(5))
```

Output

```text
00025
```

---

# Partition Methods

## partition()

Splits the string into three parts.

```python
text = "name=Prince"

print(text.partition("="))
```

Output

```python
('name', '=', 'Prince')
```

---

## rpartition()

Works like `partition()` but searches from the right.

---

# Encoding Methods

## encode()

Converts a string into bytes.

```python
text = "Python"

print(text.encode())
```

Output

```python
b'Python'
```

---

# Tabs

## expandtabs()

Replaces tabs with spaces.

```python
text = "Python\tProgramming"

print(text.expandtabs(4))
```

Output

```text
Python    Programming
```

---

# Commonly Used Methods Summary

| Method | Purpose |
|---------|---------|
| upper() | Convert to uppercase |
| lower() | Convert to lowercase |
| capitalize() | Capitalize first letter |
| title() | Capitalize each word |
| strip() | Remove spaces |
| replace() | Replace text |
| split() | Split string |
| join() | Join strings |
| find() | Find substring |
| count() | Count occurrences |
| startswith() | Check beginning |
| endswith() | Check ending |
| isalpha() | Alphabet check |
| isdigit() | Digit check |
| isalnum() | Alphanumeric check |
| center() | Center text |
| zfill() | Add leading zeros |
| partition() | Split into three parts |

---

# Common Mistakes

### Forgetting strings are immutable

Incorrect

```python
text = "python"

text.upper()

print(text)
```

Output

```text
python
```

Correct

```python
text = text.upper()
```

---

### Confusing `find()` and `index()`

- `find()` returns **-1** if the substring is not found.
- `index()` raises a **ValueError** if the substring is not found.

Choose the method based on whether you want to handle missing values gracefully.

---

# String Formatting in Python


String formatting is the process of inserting variables, values, or expressions into a string to create readable and dynamic output.

Instead of manually joining strings using the `+` operator, Python provides several formatting techniques that are easier to read, more efficient, and less error-prone.

String formatting is commonly used for:

- Displaying user information
- Printing reports
- Logging messages
- Creating file names
- Building URLs
- Formatting tables
- Automation scripts

---

# Why Use String Formatting?

Consider the following example.

Without formatting:

```python
name = "Prince"
age = 22

print("My name is " + name + " and I am " + str(age) + " years old.")
```

Output

```text
My name is Prince and I am 22 years old.
```

This works, but becomes difficult to read as the number of variables increases.

String formatting provides a cleaner solution.

---

# Methods of String Formatting

Python supports three main formatting methods.

1. Old Style Formatting (`%`)
2. `str.format()` Method
3. f-Strings (Recommended)

---

# 1. Old Style Formatting (%)

This method is inherited from the C programming language.

Although still supported, it is not recommended for new projects.

---

## Formatting Strings

```python
name = "Prince"

print("Hello %s" % name)
```

Output

```text
Hello Prince
```

---

## Formatting Integers

```python
age = 22

print("Age: %d" % age)
```

Output

```text
Age: 22
```

---

## Formatting Floating Point Numbers

```python
marks = 91.75

print("Marks: %.2f" % marks)
```

Output

```text
Marks: 91.75
```

---

## Multiple Variables

```python
name = "Prince"
age = 22

print("Name: %s Age: %d" % (name, age))
```

---

# Common Format Specifiers

| Specifier | Description |
|-----------|-------------|
| `%s` | String |
| `%d` | Integer |
| `%f` | Float |
| `%c` | Character |
| `%x` | Hexadecimal |
| `%o` | Octal |

---

# 2. str.format() Method

The `format()` method was introduced to provide a more flexible way of formatting strings.

---

## Basic Example

```python
name = "Prince"

print("Hello {}".format(name))
```

Output

```text
Hello Prince
```

---

## Multiple Variables

```python
name = "Prince"
age = 22

print("Name: {} Age: {}".format(name, age))
```

---

## Positional Arguments

```python
print("{1} {0}".format("World", "Hello"))
```

Output

```text
Hello World
```

---

## Named Arguments

```python
print("Name: {name}, Age: {age}".format(name="Prince", age=22))
```

Output

```text
Name: Prince, Age: 22
```

---

# Formatting Numbers

## Decimal Places

```python
pi = 3.14159265

print("{:.2f}".format(pi))
```

Output

```text
3.14
```

---

## Width

```python
print("{:10}".format("Python"))
```

Output

```text
Python
```

---

## Left Alignment

```python
print("{:<10}".format("Python"))
```

---

## Right Alignment

```python
print("{:>10}".format("Python"))
```

---

## Center Alignment

```python
print("{:^10}".format("Python"))
```

---

# 3. f-Strings (Recommended)

f-Strings were introduced in Python 3.6 and are now the preferred way to format strings.

They are faster, cleaner, and easier to read.

---

## Basic Example

```python
name = "Prince"

print(f"Hello {name}")
```

Output

```text
Hello Prince
```

---

## Multiple Variables

```python
name = "Prince"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

---

## Expressions

You can evaluate expressions directly inside an f-string.

```python
a = 10
b = 20

print(f"Sum = {a + b}")
```

Output

```text
Sum = 30
```

---

## Function Calls

```python
name = "python"

print(f"{name.upper()}")
```

Output

```text
PYTHON
```

---

## Formatting Floats

```python
price = 199.98765

print(f"{price:.2f}")
```

Output

```text
199.99
```

---

## Width and Alignment

### Left

```python
print(f"|{'Python':<10}|")
```

---

### Right

```python
print(f"|{'Python':>10}|")
```

---

### Center

```python
print(f"|{'Python':^10}|")
```

---

# Padding Numbers

```python
number = 25

print(f"{number:05}")
```

Output

```text
00025
```

---

# Percentage

```python
value = 0.85

print(f"{value:.0%}")
```

Output

```text
85%
```

---

# Thousands Separator

```python
number = 1000000

print(f"{number:,}")
```

Output

```text
1,000,000
```

---

# Scientific Notation

```python
number = 123456

print(f"{number:e}")
```

Output

```text
1.234560e+05
```

---

# Binary, Octal and Hexadecimal

```python
number = 25

print(f"Binary: {number:b}")
print(f"Octal : {number:o}")
print(f"Hex   : {number:x}")
```

Output

```text
Binary: 11001
Octal : 31
Hex   : 19
```

---

# Escaping Curly Braces

To print curly braces in an f-string, use double braces.

```python
print(f"{{Python}}")
```

Output

```text
{Python}
```

---

# Practical Examples

## Student Report

```python
name = "Prince"
marks = 92.75

print(f"Student: {name}")
print(f"Marks: {marks:.2f}")
```

---

## File Name

```python
day = 5

filename = f"day_{day}.txt"

print(filename)
```

---

## URL

```python
domain = "example.com"

url = f"https://{domain}"

print(url)
```

---

# Comparison

| Feature | % | format() | f-String |
|---------|---|----------|-----------|
| Easy to Read | No | Good | Excellent |
| Fast | No | Good | Best |
| Supports Expressions | No | Limited | Yes |
| Recommended | No | Yes | Yes |

---

# Common Mistakes

### Forgetting the `f`

Incorrect

```python
name = "Prince"

print("Hello {name}")
```

Output

```text
Hello {name}
```

Correct

```python
print(f"Hello {name}")
```

---

### Mixing Types with +

Incorrect

```python
age = 22

print("Age: " + age)
```

Correct

```python
print(f"Age: {age}")
```

---





# Summary

- A string is an ordered sequence of characters.
- Strings are immutable.
- Python supports indexing and slicing.
- Strings can be created using single, double, or triple quotes.
- Escape characters help represent special characters.
- Raw strings are useful for file paths and regular expressions.
- Built-in functions like `len()`, `ord()`, and `chr()` simplify string operations.
- Strings support concatenation, repetition, membership testing, and iteration.
- These methods help you format text, search for patterns, replace content, split and join strings, validate input, and align text for display.
- Python provides three methods for formatting strings: `%` formatting, `str.format()`, and **f-strings**.
---

