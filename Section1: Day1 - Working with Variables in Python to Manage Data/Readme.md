Here is the complete content formatted strictly as a Markdown file. You can copy the code block below and paste it directly into your `README.md` file.

```markdown
# 🐍 Day 1: Working with Variables in Python to Manage Data

## 📄 Overview
**Goal:** Learn the fundamentals of Python scripting, including printing to the console, inputting data, and storing data in variables.

**Final Project:** [Band Name Generator](#-final-project-band-name-generator)

---

## 📚 Concepts Learned

### 1. Printing to the Console
The `print()` function is the most basic command. It tells the computer to output something to the screen.

* **Strings:** Text in Python must be enclosed in double quotes `""` or single quotes `''`.
* **Syntax Error:** Occurs when you break the rules of the language (e.g., forgetting a closing quote).

```python
# Standard print
print("Hello World!")

# Common Error: SyntaxError (Missing quote)
# print("Hello World)

```

### 2. String Manipulation

We can manipulate how strings appear using special characters and concatenation.

* **New Line (`\n`):** Creates a line break inside a single string.
* **Concatenation (`+`):** Merges two separate strings into one.

```python
# Printing on multiple lines
print("Hello world!\nHello world!\nHello world!")

# String Concatenation (combining strings)
print("Hello" + " " + "Angela")

```

> **⚠️ Warning - IndentationError:** Python is sensitive to whitespace. Do not add spaces or tabs at the start of a line unless you are inside a block of code (like a function or loop).

### 3. The Python Input Function

The `input()` function pauses the program and waits for the user to type something. We can nest `input()` inside `print()`.

**How it works:**

1. The code executes `input(...)` first.
2. The user types data and hits Enter.
3. The `input(...)` function is **replaced** by the data the user typed.

```python
# Basic input
input("What is your name? ")

# Input inside a print statement
print("Hello " + input("What is your name? "))

```

### 4. Python Variables

Variables are like containers or labels for data. Instead of data disappearing after we use it, we can store it to use later.

```python
# Assigning input to a variable
name = input("What is your name? ")
print(name)

# Calculating length of a string using len()
length = len(name)
print(length)

```

### 5. Variable Naming Rules

To keep code clean and error-free, follow these naming conventions:

| Rule | Valid Example | Invalid Example |
| --- | --- | --- |
| **No Spaces** | `user_name` | `user name` |
| **No Numbers at Start** | `name1` | `1name` |
| **No Privileged Words** | `user_print` | `print` |
| **Use Snake Case** | `my_long_variable_name` | `MyLongVariableName` |

---

## 🎸 Final Project: Band Name Generator

### Objective

Create a program that generates a band name by combining the city the user grew up in and their pet's name.

### Example Interaction

```text
Welcome to the Band Name Generator.
What's the name of the city you grew up in?
> Bristol
What's your pet's name?
> Rabbit
Your band name could be Bristol Rabbit

```

### Solution Code

```python
# 1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")

# 2. Ask the user for the city that they grew up in.
city = input("What's the name of the city you grew up in?\n")

# 3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n")

# 4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city + " " + pet)

```

---

## 🛠️ Setup & Execution

### Step 1: Create the Python Code File

You should also have the actual executable code in this folder.
Run this command:

```bash
touch main.py

```

Then paste the code for the **Band Name Generator** (from the solution section above) into `main.py`.

### Step 2: Push to GitHub

Once you have saved these files, run these commands to update your repo:

```bash
git add .
git commit -m "Added Day 1: Variables, Inputs, and Band Name Generator Project"
git push

```

```

```