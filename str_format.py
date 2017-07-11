age = 9000
name = 'tendo'
origin = 'digital'
i = 5

print('{0} was {1} years old when he wrote this {2} script'.format(name, age, origin))
print('Why is {0} playing with that {1} reader?'.format(name, origin))
print('I am pretty sure about my {0}\n communication skills.'.format(origin))
print(i + 5)

i = i + 1
print(i)

# decimal (.) precision of x for float '0.333'
print('{0:.9f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
