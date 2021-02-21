def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 =  char+str1[1:]

  return str1

print(change_char('restart'))

def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))
