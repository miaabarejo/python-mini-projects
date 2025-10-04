# For Loops

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

    print(fruits) # notice the difference between the two
print(fruits)


# Sum
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
total_exam_score = sum(student_scores)
print(total_exam_score)

# or using loops
sum = 0
for score in student_scores:
    sum+= score
    print(sum) # maeenumerate isa isa pag naka indent
print(sum) # total na agad

# largest number
print(max(student_scores))

# or
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)


# Range Function
for number in range(1, 10): # 1 - 9 lang naprint, always add 1 if want mo mainclude ung 2nd no. like 10
    print(number)

# with steps
for number in range(1, 10, 2):
    print(number)

sum = 0
for number in range(1, 101):
    sum += number
print(sum)

# Activity OMG TAMA
number = 0
for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        continue
    elif number % 3 == 0:
        print("Fizz")
        continue
    elif number % 5 == 0:
        print("Buzz")
        continue
    print(number)