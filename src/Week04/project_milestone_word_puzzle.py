"""
REQUIREMENTS:
    Have a secret word stored in the program.
    Prompt the user for a guess.
    Continue looping as long as that guess is not correct.
    Calculate the number of guesses and display it at the end.
    You do not need to have any hints at this point.
    Final Requirements:
    In addition to the Milestone requirements, your final program must:
    Add the hints according to the rules above.
    Add a check to verify that the length of the guess is the same as the length of the secret word. 
    If it is not, display a message. If they are the same, then proceed to give the hint.
    Use a loop to generate the initial hint.
    Make sure to account for the following in your hints:
    Letters that are not present at all in the secret word (underscore _).
    Letters that are present in the secret word, but in a different spot (lowercase).
    Letters that are present in the secret word at that exact spot spot (uppercase).
"""

import random as rd

from dataclasses import dataclass


@dataclass(order=True)
class BaseSecret(object):
    word: str = rd.choice([
        'banana', 'car', 'love', 'knife', 'mouse', 'computer', 'python',
        'scriptures', 'moroni', 'nephi', 'jesus', 'subway', 'sun', 'rice',
        'beans', 'snow', 'monaliza', 'cheese'
    ])
    attempts: int = 0


class MadeYourGuess(BaseSecret):
    def __print_welcome(self):
        print("""
        @----------------------------------------------------------------------@
        @    W E L C O M E  T O  T H E  W O R D  G U E S S I N G  G A M E !    @
        @----------------------------------------------------------------------@
        \n""")

    def __generate_underscores(self):
        word_len = len(self.word) 
        return ' '.join(['_' for _ in range(word_len)])


    def __win(self):
        print('\nCongratulations! You guessed it!')
        print("""\n
          ___________    
         '._==_==_=_.'     
        .-\\:       /-.    
        | (|:.      |) |    
         '-|:.      |-'     
           \\::.   /      
            '::. .'        
              ) (          
            _.' '._        
           '-------'       
        """)

    def guess_preocessor(self):
        self.__print_welcome()
        hint = self.__generate_underscores()
        self.attempts = 0
        while True:
            print(f'\nYour hint is: {hint}')
            player_guess = str(input('What is your guess? ')).lower()
            self.attempts += 1
            if len(self.word) != len(player_guess):
                print(
                    'Sorry, the guess must have the same number of letters as the secret word.')
            elif self.word == player_guess:
                print(f'\nYour attempts/guesses: {self.attempts}')
                self.__win()
                break
            else:
                letter_and_pos = hint.split()
                intersection = list(set(player_guess) & set(self.word))
                for index, letter in enumerate(player_guess):
                    for i in intersection:
                        if letter == i and self.word.index(letter) == index:
                            letter_and_pos[index] = letter.upper()
                        if letter == i and self.word.index(letter) != index:
                            letter_and_pos[index] = letter.lower()
                hint = ' '.join(letter_and_pos)

if __name__ == '__main__':
    game = MadeYourGuess()
    game.guess_preocessor()