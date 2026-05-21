print('---simple calc---')


def add_num(x, y):
    return (x+y)


def sub_num(x, y):
    return (x-y)


def mult_num(x, y):
    return x*y


def div_num(x, y):
    try:
        return x/y
    except ZeroDivisionError as e:
        return f'error: {e}'


options = '''
1. Addition
2. subtraction
3. multiplication
4. division 
5. Quit
'''


while True:
    print('what do u want to do:')
    try:
        choice = int(input(options))
    except ValueError as e:
        print('invalid input, enter a valid number please')
        continue

    if choice == 5:
        print('calc closed')
        break

    try:
        x = float(input('enter first number: >> '))
        y = float(input('enter second number: >> '))
    except ValueError as e:
        print(e)
        continue

    if choice == 1:
        answer = add_num(x, y)
        print(f' {x} + {y} = {answer}')

    elif choice == 2:
        answer = sub_num(x, y)
        print(f' {x} - {y} = {answer}')

    elif choice == 3:
        answer = mult_num(x, y)
        print(f' {x} * {y} = {answer}')

    elif choice == 4:
        answer = div_num(x, y)
        print(f' {x} / {y} = {answer}')
