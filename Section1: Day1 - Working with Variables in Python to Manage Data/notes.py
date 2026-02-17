# -----------------------------------------------------------------------------
# Day 1: Working with Variables in Python to Manage Data
# Author: Darshan S K
# Description: Notes on printing, input, variables, and string manipulation.
# -----------------------------------------------------------------------------

# --- 1. PRINTING TO CONSOLE ---
# The print() function outputs strings to the console.
print("1. Printing:")
print("Hello World!")

# Quotes matters: You can use single '' or double "" quotes.
# print("This will cause a SyntaxError) # Missing closing quote


# --- 2. STRING MANIPULATION ---
print("\n2. String Manipulation:")

# \n creates a New Line
print("Hello world!\nHello world!\nHello world!")

# + combines (concatenates) strings
print("Hello" + " " + "Angela") # Note the space added manually in the middle


# --- 3. THE INPUT FUNCTION ---
print("\n3. Input Function:")

# input() prompts the user for data. The code pauses here until Enter is pressed.
# We can nest input() inside print().
# execution order: input() runs first -> user types -> replaced by text -> print() runs.
print("Hello " + input("What is your name? "))


# --- 4. PYTHON VARIABLES ---
print("\n4. Variables:")

# Variables store data for later use.
name = input("What is your name? ")
length = len(name) # len() calculates the number of characters in a string

print(name)
print(length)


# --- 5. VARIABLE SWAPPING LOGIC ---
print("\n5. Variable Swapping Logic:")
a = input("a: ")
b = input("b: ")

# Logic to swap two variables using a temporary third variable
c = a
a = b
b = c

print("a: " + a)
print("b: " + b)


# --- 6. VARIABLE NAMING RULES ---
# Good variable names are descriptive and follow snake_case.

user_name = "Angela"      # ✅ Valid
length1 = 10              # ✅ Valid
# 1length = 10            # ❌ Invalid (Cannot start with a number)
# user name = "Angela"    # ❌ Invalid (No spaces allowed)
# print = "Angela"        # ❌ Avoid (Don't shadow built-in function names)

print("\n--- End of Day 1 Notes ---")