def prime(number):
    if number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        return True


print(prime(int(input('Enter a number to check if it is prime: '))))
