import reeborgs_hurdle_challenge as rh
def jump():
        rh.turn_left()
        steps =0
        while wall_on_right:
            rh.move()
            steps += 1
        rh.turn_right()
        move()
        rh.turn_right()
        while steps>0:#whlle front_is_clear:
            rh.move()#     rh.move()
            steps-=1
        rh.turn_left()


while not at_goal:
    if wall_in_front():
        jump()
    elif front_is_clear:
        move()