print('''
Welcome to Treasure Island!! 
Your mission is to find the treasure''')


crossroad = input("You have arrived a crossroad, do you want to go 'left' or 'right'? \n").lower()

if crossroad=='left':
    lake = input("You have arrived a water body and it's raining \nDo you want to 'swim' or 'wait'? \n").lower()
    if lake=='wait':
        doors = input('''You have made it to the island! 
There are three doors in front of you, yellow, blue, and red only one holds the treasure.
Which door are you opening: \n''').lower()
        if doors=='yellow':
            print('''Congratulations, you have won the treasure!''')
        elif doors =='blue':
            print('You were shot to death by a marksman')
        else:
            print('You were crushed by a rock and died')
    else:
        print('You drowned in the river')
else:
    print('You entered into a forest died from a venomous snake-bite.')