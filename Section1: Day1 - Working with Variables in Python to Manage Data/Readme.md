# 🐍 Day 1: Working with Variables in Python to Manage Data

## 📄 Overview
**Goal:** Learn the fundamentals of Python scripting, including printing to the console, inputting data, debugging, and storing data in variables.
**Final Project:** [Band Name Generator](#-final-project-band-name-generator)

---

## 📚 Concepts Learned

### 1. Printing to the Console
The `print()` function is the most basic command. It tells the computer to output something to the screen.
- **Strings:** Text in Python must be enclosed in double quotes `""` or single quotes `''`.
- **Syntax Error:** Occurs when you break the rules of the language (e.g., forgetting a closing quote).

```python
# Standard print
print("Hello World!")

# Common Error: SyntaxError (Missing quote)
# print("Hello World)
2. String ManipulationWe can manipulate how strings appear using special characters and concatenation.New Line (\n): Creates a line break inside a single string.Concatenation (+): Merges two separate strings into one.Python# Printing on multiple lines
print("Hello world!\nHello world!\nHello world!")

# String Concatenation (combining strings)
print("Hello" + " " + "Angela")
⚠️ Warning - IndentationError: Python is sensitive to whitespace. Do not add spaces or tabs at the start of a line unless you are inside a block of code (like a function or loop).3. Debugging & Common ErrorsProgrammers make mistakes. The key is understanding the error message.SyntaxError: Something is typed incorrectly (e.g., missing parenthesis).IndentationError: Unexpected spaces at the start of a line.NameError: Using a variable that hasn't been defined yet (or executed).4. The Input FunctionThe input() function pauses the program and waits for the user to type something. We can nest input() inside print().How it works:The code executes input(...) first.The user types data and hits Enter.The input(...) function is replaced by the data the user typed.Python# Basic input
input("What is your name? ")

# Input inside a print statement
print("Hello " + input("What is your name? "))
5. CommentsComments are lines of code ignored by the computer. They are used to explain code to humans.Use # at the start of the line.Shortcut: Ctrl + / (Windows) or Cmd + / (Mac).Python# This is a comment
print("This is code")
6. Python VariablesVariables are like containers or labels for data. Instead of data disappearing after we use it, we can store it to use later.Python# Assigning input to a variable
name = input("What is your name? ")
print(name)

# Calculating length of a string using len()
length = len(name)
print(length)
7. Variable Naming RulesTo keep code clean and error-free, follow these naming conventions:RuleValid ExampleInvalid ExampleNo Spacesuser_nameuser nameNo Numbers at Startname11nameNo Privileged Wordsuser_printprintUse Snake Casemy_long_variable_nameMyLongVariableName🎸 Final Project: Band Name GeneratorObjectiveCreate a program that generates a band name by combining the city the user grew up in and their pet's name.Example InteractionPlaintextWelcome to the Band Name Generator.
What's the name of the city you grew up in?
> Bristol
What's your pet's name?
> Rabbit
Your band name could be Bristol Rabbit
Solution CodePython# 1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")

# 2. Ask the user for the city that they grew up in.
city = input("What's the name of the city you grew up in?\n")

# 3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n")

# 4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city + " " + pet)