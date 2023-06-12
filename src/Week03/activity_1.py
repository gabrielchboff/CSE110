first = int(input('What is the first number? '))
second = int(input('What is the second number? '))

if first > second:
    print('The first number is greater\n')
else:
    print('The first number is not greater\n')

if first == second:
    print('The numbers are equal\n')
else:
    print('The numbers are not equal\n')

if second > first:
    print('The second number is greater\n')
else:
    print('The second number is not greater\n')

user_animal = input('What is your favorite animal? ')

if user_animal.lower() == 'bear':
    print('That\'s my favorite animal too!')
else:
    print('That one is not my favorite.')
