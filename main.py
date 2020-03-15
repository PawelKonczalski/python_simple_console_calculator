import re

print('Simple calculator you can +, -, *, /')
print('Type "c" to reset result')
print('Type "quit" to exit')

result = 0
run = True


def perform_math():
    global run
    global result
    if result == 0:
        equation = input('Enter equation: ')
    else:
        equation = input(str(result)).strip()

    if equation == 'quit':
        print('Goodbye.')
        run = False
    elif equation == 'c':
        result = 0
    else:
        equation = re.sub('[a-zA-Z,:()' ']', '', equation)
        if result == 0:
            result = eval(equation)
        else:
            mathematical_operations = ['+', '-', '*', '/']
            if equation[0] in mathematical_operations:
                result = eval(str(result) + equation)
            else:
                print('You have not enter mathematical operator')


while run:
    perform_math()
