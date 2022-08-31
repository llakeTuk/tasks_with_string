
def cleaning_string(str, erase_string):
    clean_str = ''
    for symbol in str:
        if erase_string.find(symbol) == -1:
            clean_str += symbol
    print(clean_str)

y = 'y'
while y == 'y':
    origin_string = input('enter origin string: ')
    erase_string = input('enter string of numbers to erase: ')
    cleaning_string(origin_string, erase_string)
    y = input('restart?(y/n): ')
