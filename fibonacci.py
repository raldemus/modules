# import fibonacci
#
#
# fibonacci.hello()
# print('What numbers do you want to calculate?')
# print('Fibonacci =', fibonacci.fib(int(input())))


def hello():
    print('This is an example of Fibonacci Numbers.')


def fib(n):
    a = b = 1
    for i in range(n-2):
        a, b = b, a+b
    return b
