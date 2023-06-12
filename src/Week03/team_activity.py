grade_percentage = int(input('What is your grade percent? '))
letter = ''
sign = ''

if (grade_percentage >= 90):
    letter = 'A'
elif (grade_percentage >= 80):
    letter = 'B'
elif (grade_percentage >= 70):
    letter = 'C'
elif (grade_percentage >= 60):
    letter = 'D'
else:
    letter = 'F'

last_digit = grade_percentage % 10
# or: last_digit = int(repr(grade_percentage)[-1])

if (last_digit >= 7):
    sign = '+'
elif (last_digit < 3):
    sign = '-'
else:
    sign = ''

if (grade_percentage >= 93):
    sign = ''

if (letter == 'F'):
    sign = ''


print(f'Your letter grade is: {letter}{sign}')

if (grade_percentage >= 70):
    print('Congratulations! You passed the class!')
else:
    print('You don\'t have a sufficeinte grade, you need to work on!')
