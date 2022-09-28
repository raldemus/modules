def arithmetic(first_number, operation, second_number):
    if operation == '+':
        print('Result:', first_number + second_number)
    elif operation == '-':
        print('Result:', first_number - second_number)
    elif operation == '*':
        print('Result:', first_number * second_number)
    elif operation == '/':
        print('Result:', first_number / second_number)
    else:
        print('Unknown operation')


print(arithmetic(int(input('Input first number: ')), input('Choose operation symbol: '),
                 int(input('Input second number: '))))
