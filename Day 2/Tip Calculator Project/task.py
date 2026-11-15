print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage = bill * (tip / 100)

total = (bill  + tip_percentage) / people

print(f"Each person should pay: ${round(total, 2)}")
