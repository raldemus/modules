def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


print(is_year_leap(int(input('Enter the year to check if it is a leap year: '))))
