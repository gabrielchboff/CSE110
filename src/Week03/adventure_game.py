
import random
import os


class Menu(object):

    @staticmethod
    def show():
        print("""
        |----------------------------------------|
        |                                        |
        |        F I N D  T H E  R U B Y !       |
        |                                        |
        |            Start ? (YES/NO)            |
        |----------------------------------------|            
        """)
    @staticmethod
    def get_option():
        inp = str(input('> ')).lower()
        if inp == 'no':
            quit()
        elif inp == 'yes':
            print('\nWelcome to The Quest for the Ruby!')
        else:
            print('Please type YES or NO.')

class Quest(object):

    def __init__(self):
        self.actions = [
            'look for clues',
            'explore the surroundings',
            'search for the ruby',
            'talk to the locals',
            'rest and regain strength'
        ]
        self.situations = [
            'You find a hidden passage leading into a dark cave.',
            'You come across a group of hostile knights.',
            'You stumble upon a village that has been destroyed.',
            'You encounter a wise old man who offers you advice.',
            'You get lost in a dense forest and can\'t find your way out.'
        ]

    def clear_screen(self):
        host = str(os.uname()[0]).lower()
        if host == 'linux' or host == 'macos':
            os.system('clear')
        elif host == 'windows':
            os.system('cls')
        else:
            os.system('clear')
            

    def start(self):
        self.player_name = input('\nWhat is your name? ')
        print(f'\nWelcome, {self.player_name}! Your quest is to find the Ruby.')
        self.current_situation = random.choice(self.situations)
        self.clear_screen()
        self.play()

    def play(self):
        while True:
            print('\nWhat do you want to do?')
            for i, action in enumerate(self.actions):
                print(f'{i+1}. {action}')
            choice = input('\nEnter a number > ')
            if choice == '1':
                self.look_for_clues()
            elif choice == '2':
                self.explore_surroundings()
            elif choice == '3':
                self.search_for_ruby
            elif choice == '4':
                self.talk_to_locals()
            elif choice == '5':
                self.rest_and_regain_strength()
            else:
                print('Invalid choice. Please enter a number between 1 and 5.')

    def look_for_clues(self):
        print('\nYou search for clues...')
        result = self.generate_situation()
        print(result)

    def explore_surroundings(self):
        print('\nYou explore the surroundings...')
        result = self.generate_situation()
        print(result)

    def search_for_rub(self):
        print('\nYou search for the ruby...')
        result = self.generate_situation()
        print(result)
    
    def talk_to_locals(self):
        print('\nYou talk to the locals...')
        result = self.generate_situation()
        print(result)

    def rest_and_regain_strength(self):
        print('\nYou rest and regain strength...')
        print('\nYou found a potion of strength!')
        result = self.generate_situation()
        print(result)

    def generate_situation(self):
        print('\nYou found a map!Do you want follow the map?(YES/NO)) \n')
        decision = str(input('> ')).lower()

        if decision == 'no':
            print('You encounter a pack of wolves!')
            print('What do you do?(FIGHT/ RUNS)')

        
            decision = str(input('> ')).lower()
            while True:

                if decision == 'fight':
                    print('You fight off the wolves and continue on your journey.')
                    break
                elif decision == 'run':
                    print('You try to run, but the wolves catch you and you lose the game.')
                    return

            print('You continue through the forest.')
            print('You come across a river.')
            print('What do you do?(SWIM/BUILD A RAFT)')

            while True:
                decision = str(input('> ')).lower()

                if decision == 'swim':
                    print('You swim across the river and continue on your journey.')
                    break
                elif decision == 'build a raft':
                    print('You build a raft and cross the river safely.')
                    break

            print('You continue through the forest.')
            print('You come across a fork in the road.')
            print('What do you do?(GO LEFT/GO RIGHT)')

            decision = str(input('> ')).lower()

            if decision == 'go left':
                self.win_game() 
                return
            elif decision == 'go right':
                print('You come across a band of bandits.')
                print('They rob you and you lose the game.')
                return

        elif decision == 'go right':
            print('You come across a swamp.')
            print('What do you do?(WALK THROUGH/GO AROUND)')

            while True:
                decision = str(input('> ')).lower()

                if decision == 'walk through':
                    print('You get stuck in the mud and lose the game.')
                    return
                elif decision == 'go around':
                    print('You successfully navigate around the swamp.')
                    break

            print('You continue through the forest.')
            print('You come across a fork in the road.')
            print('What do you do?(GO LEFT/GO RIGHT)')

            decision = str(input('> ')).lower()

            if decision == 'go left':
                print('You come across a friendly merchant who sells you a powerful weapon.')
                print('You continue on your journey.')
                self.play()
            elif decision == 'go right':
                print('You fall into a trap and lose the game.')
                return

        elif decision == 'no':
            self.play()
    
        else:
            print('Invalid decision. Try again.')

    def win_game(self):
        self.clear_screen()
        print(f'\nCongratulations, {self.player_name}! You have found the Ruby and completed your quest.')
        print('Thanks for playing!')
        exit()

Menu.show()
Menu.get_option()
quest = Quest()
quest.start()
