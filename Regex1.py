#!/usr/bin/python
import re

# '.' means any char
# page 115 in the book
# X? match 0 or 1 occurrences of x
# X+ match 1 or more occurrences of x
# X* match 0 or more occurrences of x
# X{3} match 3 occurrences of x
# X{m, n} match between m and n occurrences of x
# abc match abc
# abc|xyz match abc or xyz
pattern = re.compile('.')
text = '123654111321'
res = pattern.match(text)
print(res)

res = pattern.search(text)
print(res)

res = pattern.findall(text)
print(res)

alpha_pattern = re.compile('[a-zA-Z]')
res = alpha_pattern.findall(text)
print(res)

text2 = "z1234asdffgrg456a"
res = alpha_pattern.findall(text2)
print(res)

numeric_pattern = re.compile('[0-9]')
res = numeric_pattern.findall(text2)
print(res)

last_char_is_num_pattern = re.compile('[0-9]$')
res = last_char_is_num_pattern.findall(text2)
print(res)
res = last_char_is_num_pattern.findall(text)
print(res)

first_char_is_num_pattern = re.compile('^[0-9]')
res = first_char_is_num_pattern.findall(text2)
print(res)
res = first_char_is_num_pattern.findall(text)
print(res)

or_pattern = re.compile('12|df')
res = or_pattern.findall(text2)
print(res)
res = or_pattern.findall(text)
print(res)

phone_num = '09-7718392'
phone_num_pattern = re.compile('^0[234589]\-?[1-9][0-9]{6}$')
res = phone_num_pattern.findall(phone_num)
print(res)

cell_num = '052-1784218'
cell_phone_num_pattern = re.compile('^05[02458]\-?[1-9][0-9]{6}$')
res = cell_phone_num_pattern.findall(cell_num)
print(res)
