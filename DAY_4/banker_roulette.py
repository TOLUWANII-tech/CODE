names_string = input("Give me everybody's name, with each separated by a comma \n")
names = names_string.split(', ')


import random
index = len(names)-1
random_name = random.randint(0, index)


print(f"{names[random_name]} is going to pay the bills today")

#random.choice(list) will also pick a random value from a list