# 🔢 Day 2: Data Types, Numbers, Operations & Type Conversion

# ------------------------------------------------------------------
# 1. PRIMITIVE DATA TYPES
# ------------------------------------------------------------------
# Python has several built-in data types.

# String (str): A sequence of characters enclosed in quotes.
print("Hello"[0])       # Subscripting: Pulling out the character at index 0 ('H')
print("Hello"[-1])      # Negative Indexing: Pulling out the last character ('o')

# Integer (int): Whole numbers.
print(123 + 345)        # Mathematical addition (Result: 468)
print(123_456_789)      # Underscores are ignored by Python (Result: 123456789)

# Float (float): Numbers with decimal places.
print(3.14159)

# Boolean (bool): True or False.
print(True)
print(False)

# ------------------------------------------------------------------
# 2. TYPE CHECKING & TYPE CONVERSION
# ------------------------------------------------------------------

num_char = len(input("What is your name? "))

# Type Checking: Check the data type of a variable
print(type(num_char))   # <class 'int'>

# Type Conversion (Casting): Changing a piece of data from one type to another
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))          # <class 'float'>

print(70 + float("100.5")) # Result: 170.5

# ------------------------------------------------------------------
# 3. MATHEMATICAL OPERATIONS
# ------------------------------------------------------------------

print(3 + 5)            # Addition
print(7 - 4)            # Subtraction
print(3 * 2)            # Multiplication
print(6 / 3)            # Division (Always returns a float)
print(2 ** 3)           # Exponent (2 to the power of 3)

# PEMDAS (Order of Operations):
# Parentheses ()
# Exponents **
# Multiplication * & Division / (Left to Right)
# Addition + & Subtraction - (Left to Right)

print(3 * 3 + 3 / 3 - 3)
# 1. 3 * 3 = 9
# 2. 3 / 3 = 1.0
# 3. 9 + 1.0 = 10.0
# 4. 10.0 - 3 = 7.0

# ------------------------------------------------------------------
# 4. NUMBER MANIPULATION & F-STRINGS
# ------------------------------------------------------------------

# Rounding
print(round(8 / 3))     # Rounds to nearest whole number (3)
print(round(8 / 3, 2))  # Rounds to 2 decimal places (2.67)

# Floor Division (//)
print(8 // 3)           # Chops off the decimal part (Result: 2)

# F-Strings: Mix strings and different data types easily
score = 0
height = 1.8
isWinning = True

# f-String Syntax: f"String {variable}"
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")