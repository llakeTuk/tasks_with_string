def search_substr(str, substr):
  if sybstr in str:
    print('substring is in string')
  else:
    print('there is no substring in string')
y = 'y'
while y == 'y':
  input_str = input('enter main string: ')
  input_substr = input('enter substring: ')
  search_substr(input_str, input_substr)
  y = input('restart?(y/n): ')
print('goodbye')
