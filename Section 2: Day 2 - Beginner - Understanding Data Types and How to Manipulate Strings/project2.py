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