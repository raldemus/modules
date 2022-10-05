file = open(input('Enter file name: '))
string = file.read()
file.close()
template = '''{} bottles of beer on the wall.
Take one down and pass it around, {} bottles of beer on the wall.'''
count = 0
for i in string.upper():
    if i == 'H':
        print('Hello, world!')
    elif i == 'Q':
        print(string)
    elif i == '9':
        for bottles in range(99, 1, -1):
            print(template.format(bottles, bottles-1))
        print('1 bottle of beer on the wall.\nTake one down and pass it around,'
              ' no more bottles of beer on the wall.')
        print('No more bottles of beer on the wall.\nGo to the store and buy some more,'
              ' 99 bottles of beer on the wall.')
    elif i == '+':
        count += 1
