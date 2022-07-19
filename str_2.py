
def first_and_last(letter, str):
  if str.find(letter) < 0:
    return None, None
  return str.find(letter) + 1, str.rfind(letter) + 1
y = 'y'
while y == 'y':
  input_str = input('enter main string: ')
  input_letter = input('enter letter to find in string: ')
  print(first_and_last(input_letter, input_str))
  y = input('restart?(y/n): ')