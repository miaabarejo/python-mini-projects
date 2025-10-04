print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?")) #float or int pwede
total_of_people = int(input("How many people to split the bill?"))
bill_with_tip = total_bill + (total_bill * tip / 100)
bill_per_person = bill_with_tip / total_of_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
