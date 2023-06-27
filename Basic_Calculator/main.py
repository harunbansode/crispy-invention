def addition(num1, num2):
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
    return result


def subtraction(num1, num2):
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')
    return result


def multiply(num1, num2):
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')
    return result


def divison(num1, num2):
    result = num2 / num1
    print(f'{num2} / {num1} = {result}')
    return result

print('Welcome to Calculator')
print('A for Addition')
print('B for Subtraction')
print('C for Multiplication')
print('D for Division')
print('E for Exit')

while True:
    user = input('Enter the symbol: ')
    if user.capitalize() == 'A':
        print('Addition:')
        a = int(input('Num1: '))
        b = int(input('Num2: '))
        addition(a, b)

    elif user.capitalize() == 'B':
        print('Subtraction:')
        a = int(input('Num1: '))
        b = int(input('Num2: '))
        subtraction(a, b)

    elif user.capitalize() == 'C':
        print('Multiplication:')
        a = int(input('Num1: '))
        b = int(input('Num2: '))
        multiply(a, b)

    elif user.capitalize() == 'D':
        print('Division:')
        a = int(input('Num1: '))
        b = int(input('Num2: '))
        divison(a, b)

    elif user.capitalize() == 'E':
        print('Program ended')
        quit()