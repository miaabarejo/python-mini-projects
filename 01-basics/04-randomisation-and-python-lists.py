# Mersenne Twister - very complicated
#Pseudorandom number generator

import random
import my_module

random_integer = random.randint(1, 10) #no need to input a: (magkukusa na siya)
print(random_integer)


# Module
# splitting the code into individual modules

print(my_module.my_favourite_number)


import random

random_number_0_to_1 = random.random() #1st random is module, 2nd is a function (0 to 1 lang ung sakop nito)
print(random_number_0_to_1)


#expand
import random

random_number_0_to_1 = random.random() * 10 # 0 to 10, not inclusive of 10
print(random_number_0_to_1)


# random floating point number generator
import random

# inclusive of a and b
random_float = random.uniform(1,10)
print(random_float)


# Activity (TAMA AKO YEHEY)
import random

head_or_tail = random.randint(0,1)
if head_or_tail == 0:
    print("Head")
else:
    print("Tail")


# List (isang variable nalang ung gagamitin, BUT THEY ALSO HAVE AN ORDER)
states_of_america = ["Delaware", "Pennysylvania", "New Jersey"]
print(states_of_america[0]) #no starts with 0
# you can use negative, start ka lang ng bilang sa dulo, there is no -0 lol


# Alter items inside the list
states_of_america = ["Delaware", "Pennysylvania", "New Jersey"]
states_of_america[1] = "Pencilvania" # like kunwari icachange ung spelling ganun
print(states_of_america)


# Add to the list, TO THE END OF THE LIST
states_of_america = ["Delaware", "Pennysylvania", "New Jersey"]
states_of_america.append("Angelaland")
print(states_of_america)


# Add a WHOLE BUNCH of items to the end of the list
states_of_america = ["Delaware", "Pennysylvania", "New Jersey"]
states_of_america.extend(["Angelaland", "Jack Bauer Land"])
print(states_of_america)


# Activity, based on my understanding and dun sa naituro
import random

friends = random.randint(0,4)
if friends == 0:
    print("Alice")
elif friends == 1:
    print("Bob")
elif friends == 2:
    print("Charlie")
elif friends == 3:
    print("David")
else:
    print("Emanuel")


# Other way, hindi pa naturo

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))

# Other way pa
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_index = random.randint(0, 4)
print(friends[random_index])


# IndexErrors and Working with Nested lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables] # we now have a list that contains 2 lists
print(dirty_dozen)


# Quiz #3
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1]) # ung unang 1 ung veg, kasi 0 ung fruits (0, 1) tapos 1 sa veggies ay ung kale gets gets