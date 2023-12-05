logo = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''





def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation from the line above: ")

    num2 = float(input("What's the second number? "))

    function = operations[operation_symbol]

    answer = function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    go_on = True

    while  go_on:


        another_round = input(f"Do you want to continue with {answer} as your first number? Type 'y' for  and 'n' for no")
        if another_round =='n':
            go_on = False
            calculator()

        operation_symbol = input("Pick another operation: ")
        num1=answer
        num2 = float(input("Choose another number: "))

        function = operations[operation_symbol]

        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")


calculator( )





