# 🔢 Day 2: Understanding Data Types and String Manipulation

## 📄 Overview
**Goal:** Learn about primitive data types, mathematical operations, type conversion, and f-strings to build a calculator.
**Final Project:** [Tip Calculator](#-final-project-tip-calculator)

---

## 📚 Concepts Learned

### 1. Primitive Data Types
Python has 4 main primitive data types. You can check the type of any variable using the `type()` function.

| Data Type | Keyword | Description | Example |
| :--- | :--- | :--- | :--- |
| **String** | `str` | A string of characters. | `"Hello"` |
| **Integer** | `int` | Whole numbers (no decimals). | `123` |
| **Float** | `float` | Floating point number (decimals). | `3.14` |
| **Boolean** | `bool` | True or False values. | `True` |

```python
# Integer (can use underscores for readability)
print(123_456) 

# Float
print(3.14159)

# Boolean
print(True)

```

### 2. Subscripting (String Slicing)

You can pull out individual characters from a string using square brackets `[]`. Programmers always start counting from **0**.

* **Index 0:** First character.
* **Negative Index:** Counts backwards from the end.

```python
print("Hello"[0])  # Prints 'H'
print("Hello"[4])  # Prints 'o'

# Negative indexing 
print("Hello"[-1]) # Prints 'o' (last character)

```

### 3. Type Conversion (Casting)

You cannot mathematically add a string to a number. You must convert data types explicitly to avoid a `TypeError`.

* `str()`: Converts to String.
* `int()`: Converts to Integer.
* `float()`: Converts to Float.

```python
num_char = len(input("What is your name?"))

# incorrect: print("Your name has " + num_char + " characters.") -> TypeError
# correct:
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# Other conversions:
print(70 + float("100.5"))  # Result: 170.5

```

### 4. Mathematical Operations

Python follows the standard mathematical order of operations (**PEMDAS**: Parentheses, Exponents, Multiply/Divide, Add/Subtract).

| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| `+` | Addition | `3 + 5` | `8` |
| `-` | Subtraction | `7 - 4` | `3` |
| `*` | Multiplication | `3 * 2` | `6` |
| `/` | Division | `6 / 3` | `2.0` (Always a float) |
| `**` | Exponent | `2 ** 3` | `8` () |
| `//` | Floor Div | `8 // 3` | `2` (Chops off decimal) |

**Priority Rule:**

1. **()** Parentheses
2. ****** Exponents
3. ***/ /** Multiplication & Division (Left to Right)
4. **+ -** Addition & Subtraction (Left to Right)

```python
print(3 * 3 + 3 / 3 - 3) 
# Step 1: 3 * 3 = 9
# Step 2: 3 / 3 = 1.0
# Step 3: 9 + 1.0 = 10.0
# Step 4: 10.0 - 3 = 7.0

```

### 5. Number Manipulation & f-Strings

Working with numbers often requires rounding or formatting strings cleanly.

* **Rounding:** `round(number, digits)`
* **Assignment Operators:** `+=`, `-=`, `*=`, `/=`
* **f-Strings:** Insert variables directly into strings using `{}`.

```python
# Rounding
print(round(8 / 3, 2))  # Result: 2.67

# Assignment Operator
score = 0
score += 1 # Same as score = score + 1

# f-Strings (The easy way to print)
height = 1.8
is_winning = True
print(f"Your score is {score}, height is {height}, winning is {is_winning}")

```

---

## 💰 Final Project: Tip Calculator

### Objective

Create a program that calculates how much each person needs to pay when splitting a bill, including a specific tip percentage.

### Example Interaction

```text
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
Each person should pay: $19.93

```

### Solution Code

```python
# 1. Create a greeting for your program.
print("Welcome to the tip calculator!")

# 2. Get user input and convert to correct data types
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# 3. Calculate total bill with tip
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

# 4. Calculate bill per person
bill_per_person = total_bill / people

# 5. Round to 2 decimal places using format (better for currency)
final_amount = "{:.2f}".format(bill_per_person)

# 6. Print result
print(f"Each person should pay: ${final_amount}")

```

```

```