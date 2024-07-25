# Python_Portfolio
Python projects on PyCharm

from datetime import date

name = input('Enter name here:\n')
age = int(input('Enter age here:\n'))

current_year = date.today().year

user_age = current_year - age

print('What is your name?', name)
print('How old are you?', age)
print('\nHello {name}! You were born in {year}.'.format(name=name, year=user_age))

OUTPUT:

Enter name here:
Patty
Enter age here:
33
What is your name? Patty
How old are you? 33

Hello Patty! You were born in 1991.

Process finished with exit code 0
