def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


def date(day, month, year):
    days_in_month = {1: 31,
                     2: 29 if is_year_leap(year) else 28,
                     3: 31,
                     4: 30,
                     5: 31,
                     6: 30,
                     7: 31,
                     8: 31,
                     9: 30,
                     10: 31,
                     11: 30,
                     12: 31}
    if 1 <= month <= 12 and 1 <= day <= days_in_month[month]:
        return True
    return False


def date_module(day, month, year):
    import datetime
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    else:
        return True


print(date(int(input("Enter the day: ")), int(input("Enter the month: ")),
           int(input("Enter the year: "))))
