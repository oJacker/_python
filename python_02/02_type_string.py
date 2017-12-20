# -*- coding: utf-8 -*-

import string
s = ' abcd efg '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s)

# string concatenation

print('abc_' + 'defg')
s = 'abcdefg'
s += '\nhijk'
print(s)


# Caps look

s = 'abc defg'
print(s.upper())
print(s.upper().lower())
print(s.capitalize())
print(s.title())

# location and cmp

s_1 = 'abcdefg'
s_2 = 'abdefgh'
print(s_1.index('bcd'))


try:
    print(s_1.index('bce'))
except ValueError:
    print('ValueError: substring not found')


print(s_1 == s_1)
print(s_1 > s_2)
print(s_2 > s_1)
 


# split and join
s = 'abc,def,ghi'
print(s.split(','))
s = '123\n456\n789'

numbers = s.splitlines()
print(numbers)
print('-'.join(numbers))


# Commonly used judgment

s = 'abcdefg'
print(s.startswith('abc'))
print(s.endswith('efg'))
print('abcd1234'.isalnum())
print('\tabcd1234'.isalnum())
print('abcd'.isalpha())
print('12345'.isdigit())
print('   '.isspace())
print('acb125'.islower())
print('A1B2C'.isupper())
print('Hello world!'.istitle())




#number to string
print(str(5))
print(str(5.))
print(str(-5.23))
print(int('1234'))
print(float('-23.456'))

#format(string)

print('Hello %s!' % 'world')
print('%d-%.2f-%s' % (4, -2.3, 'hello'))




















