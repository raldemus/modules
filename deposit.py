def bank(money, years):
    for i in range(years):
        money *= 1.1
    return money


print(bank(int(input('Enter the initial capital invested in the bank: ')),
           int(input('Enter the number of years the money will be kept in the bank: '))))
