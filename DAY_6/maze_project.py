import reeborgs_hurdle_challenge as rh


while front_is_clear():
    rh.move()
#turnn_left

while not at_goal():
    if right_is_clear():
        rh.turn_right()
        rh.move()
    elif wall_on_right():
        if front_is_clear():
            rh.move()
        elif wall_in_front():
            rh.turn_left()
    