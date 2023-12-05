import reeborgs_hurdle_challenge as rh 

def jump():
    rh.turn_left()
    rh.move()
    rh.turn_right()
    rh.move()
    rh.turn_right()
    rh.move()
    rh.turn_left()

while not at_goal:
    if front_is_clear():
        rh.move()
    elif wall_in_front:
        jump()
