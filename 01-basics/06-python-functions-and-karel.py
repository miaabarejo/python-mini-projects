#defining functions
def my_function():
    print("Hello")
    print("Bye")
my_function()

 #Reeborg's World hurdle loop
 def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()

#While Loop
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

#hurdle2
while at_goal() != True: #pwede rin while not at_goal():
    jump()

#hurdle3
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#hurdle4
 def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#maze
 def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()