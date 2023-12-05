from math import ceil

def paint_calc(height, width, cover):
    paint_cans = (height*width)/cover
    number_of_paint_cans = ceil(paint_cans)
    print(f"You'll need {number_of_paint_cans} cans of paint")


test_h = int(input('Height of wall (m): '))
test_w = int(input("Width of wall(m): "))


coverage = 5

paint_calc(height = test_h, width=test_w, cover = coverage)