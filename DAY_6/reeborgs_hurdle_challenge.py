def move():
    return "I have moved"

def turn_left():
    return 'I have tured left'


def turn_right():
    turn_left_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump( )