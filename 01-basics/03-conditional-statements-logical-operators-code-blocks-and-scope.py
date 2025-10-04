# If Else
print("Welcome to the rollercoaster")
height = int(input("Please enter your height: "))

if height >= 120: # >, <, >=, <=, ==, == uses for exact numbers
    print("You can ride the rollercoaster") #indented = block of code, lives inside the if statement
else:
    print("Sorry, you have to grow taller before you can ride the rollercoaster.")


# Modulo Operator % (remainder)
# like 10 % 5 = 0 (10 / 5 = 2)

# Activity - Check Odd or Even
number = int(input("Input the number:"))
if number % 2 == 0:
    print("The number is an even number.")
else:
    print("The number is an odd number.")


# Nested if / else

# Activity
height = int(input("Please enter your height: "))
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("Input your age: "))
    if age <= 18:
        print("You need to pay $7")
    else:
        print("You need to pay $12")
else:
    print("You can't ride the rollercoaster.")

# Activity Elif
height = int(input("Please enter your height: "))
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("Input your age: "))
    if age <= 12:
        print("You need to pay $5")
    elif age <= 18: # else if
        print("You need to pay $7")
    # elif age < 22: (can add as many as you can, magstart sa baba pataas na number)
    else:
        print("You need to pay $12")
else:
    print("You can't ride the rollercoaster.")


# Coding Exercise: BMI Calculator with Interpretations
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("normal weight")
else:
    print("overweight")


# Multiple If Statements
height = int(input("Please enter your height: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("Input your age: "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18: # else if
        bill = 7
        print("Youth tickets are $7")
    # elif age < 22: (can add as many as you can, magstart sa baba pataas na number)
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Would you like have a photo take? Type y for Yes and n for No: ")
    if wants_photo == "y":
        # Add $3 to their bill
        bill += 3 # same as bill = bill + 3

    print(f"Your final bill is: ${bill}")
else:
    print("You can't ride the rollercoaster.")


# Pizza Order Practice
print("Welcome to Python Pizza Deliveries!")
size = input("What pizza size do you want? S, M, or L ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


# Logical Operators

height = int(input("Please enter your height: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("Input your age: "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18: # else if
        bill = 7
        print("Youth tickets are $7")
    # elif age < 22: (can add as many as you can, magstart sa baba pataas na number)
    elif age >= 45 and age <= 55: # or 45 <= age <= 55:
        print("Everything is going to be okay. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Would you like have a photo take? Type y for Yes and n for No: ")
    if wants_photo == "y":
        # Add $3 to their bill
        bill += 3 # same as bill = bill + 3

    print(f"Your final bill is: ${bill}")
else:
    print("You can't ride the rollercoaster.")


# Quiz

a = 5
b = 7

if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")