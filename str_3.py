from collections import Counter
def most_counted(str, size_of_top):
  counter_top = Counter(str.replace(' ', '')).most_common(size_of_top)
  return ', '.join([f'{letter} - {count}' for letter, count in counter_top])
y = 'y'
while y == 'y':
  input_str = input('enter string: ')
  input_int = int(input('enter size of most common letters in string: '))
  print(most_counted(input_str, input_int))
  y = input('restart?(y/n): ')
print('goodbye')
