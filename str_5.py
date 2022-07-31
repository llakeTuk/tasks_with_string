def string_letter_sort(enter_str):
  vowel_str = ''
  consonant_str = ''
  alpha_string = 'aeioyqwrtupsdfghjklzxcvbnm '
  for letter_number in range(len(enter_str)):
    place_finder = alpha_string.find(enter_str[letter_number])
    if place_finder >= 0:
      if place_finder < 4:
        vowel_str += enter_str[letter_number]
        consonant_str += ' '
      else:
        vowel_str += ' '
        consonant_str += enter_str[letter_number]
    else:
      vowel_str += ' '
      consonant_str += ' '
  print(consonant_str)
  print(vowel_str)
y = 'y'
while y == 'y':
  input_str = input('enter string: ')
  string_letter_sort(input_str)
  y = input('restart?(y/n): ')
print('goodbye')
