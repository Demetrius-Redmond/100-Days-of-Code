print("Welcome to the tip calculator! ")  
bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ") 
people = input("How many people to split the bill? ")
bill = float(bill)
tip = float(tip)
people = int(people)
final_amount = (bill * (tip / 100 + 1.0)) / people
print(f"Each person should pay: ${round(final_amount, 2)}")

# multiply number by 1.(.tip)divided by people round to 2 decimal places

