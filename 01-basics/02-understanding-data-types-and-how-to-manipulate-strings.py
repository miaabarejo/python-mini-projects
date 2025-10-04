# Subscripting
print("Hello"[4])

print("Hello"[-1])

# Integer
print(123 + 345)

print(123_456_789)

# Float (decimal)
print(3.14159)

# Boolean
print(True)
print(False)

# Quiz
street_name = "Abbey Road"
print(street_name[4] + street_name[7])

# Check data type
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

# Exercise
# print("Number of letters in your name: " + len(input("Enter your name")))

name = input("What is your name?")
length = len(name)

print(type(name)) #str
print(type(length)) #int

print("Number of letters in your name: " + str(length))

# Mathematical Operations
print("My age is: " + str(22))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3) #default w/ decimal, considered as FLOAT
print(6 // 3) #w/o decimal
print(2**3) #2 raised to 3

# PEMDAS

# ()
# **
# * OR /
# + OR -

print (3 * 3 + 3 / 3 - 3) #by pair ung pagsolve here

# Exercise
print (3 * (3 + 3) / 3 - 3)

# Number Manipulation
bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi)) #removes decimal
print(round(bmi)) #rounds off decimal number
print(round(bmi, 2)) #no of digits you want to round off, like 2 decimal places

score = 0
# User scores a point
score += 1
print(score)

# f-strings
print("Your score is: " + str(score))

score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

# Quiz
print(6 + 4 /2 - (1 * 2))

a = int("5") / int (2.7)
print(a)

name = input("What is your name?")
print(f"Hello, {name}")
print("Hello, " + name)

age = 12
# print("Your are " + age + " years old.") = WRONG, it should be str(age)




