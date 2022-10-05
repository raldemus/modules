from math import sqrt


def square(side):
    p = 4*side
    s = side**2
    d = side*sqrt(2)
    t = (p, s, d)
    print(t)


print(square(int(input('Enter the length of the side of the square: '))))
