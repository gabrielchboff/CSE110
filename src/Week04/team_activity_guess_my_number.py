import random as rd

print("""
****************************************

Welcome to guess my number!
Try to guess a number between 1 and 10.

****************************************
""")

magic_number = int(input('What is the magic number? '))
guess = 0
total_guess = 0
while magic_number != guess:
    guess = int(input('What is your guess? '))
    total_guess += 1
    if guess == magic_number:
        print('You guessed it!\n')
    elif guess < magic_number:
        print('Higher\n')
    else:
        print('Lower\n')
print(f'You made {total_guess} guesses.\n')
print('\nNow you will try the level hard!\nYou need to guess a nember between 1 and 100!\n')

magic_number = rd.randint(1, 100)
guess = 0
total_guess = 0
while True:
    guess = int(input('What is your guess? '))
    total_guess += 1
    if guess == magic_number:
        print('You guessed it!\n')
        print(f'You made {total_guess} guesses.\n')
        quit_or_continue = str(input('Do you want to continue? (YES/NO) ')).lower()
        if quit_or_continue == 'no':
            break
        else:
            magic_number = rd.randint(1, 100)
            total_guess = 0
            guess = 0
    elif guess < magic_number:
        print('Higher\n')
    else:
        print('Lower\n')
