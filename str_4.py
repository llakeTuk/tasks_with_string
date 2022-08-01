def str_fence(str):
  letter_counter = 0
  output_str = ''
  for letter in str:
    if letter.isalpha():
      if letter_counter % 2 == 0:
        output_str += letter.upper()
      else:
        output_str += letter.lower()
      letter_counter += 1
    else:
      output_str += letter
  return output_str
y = 'y'
while y == 'y':
  input_str = input('enter string: ')
  print(str_fence(input_str))
  y = input('restart?(y/n): ')
print('goodbye')
