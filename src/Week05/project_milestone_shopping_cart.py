
import ast
import base64
import os

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True, order=True)
class ShoppingCart(object):
    cart: list = field(default_factory=list)
    PRICE: int = 1
    NAME: int = 0

    def add_item(self) -> None:
        item = str(input('What item would you like to add? '))
        price = float(input(f"What is the price of '{item}'? "))
        self.cart.append([item, price])
        print(f"'{item}' has been added to the cart.")

    def view_cart(self) -> None:
        print('The contents of the shopping cart are:')
        if len(self.cart) != 0:
            for index, item in enumerate(self.cart):
                print(f'{index+1}. {item[self.NAME]} - ${item[self.PRICE]:.2f}')
        else:
            print('Your cart is empty! Please add some items.')

    def remove_item(self) -> None:
        item = int(input('Which item would you like to remove? '))
        if (len(self.cart) < item):
            print('Sorry, that is not a valid item number.')
        else:
            index = item - 1
            self.cart.pop(index)
            print('Item removed.')

    @property
    def total(self) -> float:
        total_prices = [i[self.PRICE] for i in self.cart]
        return round(sum(total_prices), 2)

    def quit(self) -> None:
        print('Thank you. Goodbye.')

    @staticmethod
    def welcome(self, user: str) -> None:
        print(f"""
        -----------------------------------

        WELCOME {user} TO THE SHOPPING CART!

        Please select one of the following:
        1. Add item
        2. View cart
        3. Remove item
        4. Compute total
        5. Quit

        -----------------------------------
        """)


@dataclass(order=True)
class User(object):
    username: str = field(default_factory=str)
    password: str = field(default_factory=str)
    cart: ShoppingCart = field(default_factory=ShoppingCart)
    USER_POS: int = 0
    PASS_POS: int = 1

    def login_display(self) -> int:
        print("""
        ---------------------------------

        WELCOME TO SHOPPING CART!

        Chose one of this options:
        1. Register.
        2. Login.
        3. Quit.

        ---------------------------------
        """)
        opt = int(input('Type your option: '))
        return opt

    def __exists_user(self) -> bool:
        if not os.path.isfile('login.txt'):
            with open('login.txt', 'w') as f:
                f.write('')

        with open('login.txt', 'rb') as f:
            logins = [
                ast.literal_eval(
                    base64.b64decode(login).decode('ascii')
                )
                for login in f.readlines()
            ]
            logins = [login[self.USER_POS] for login in logins]
            if self.username in logins:
                return True
            else:
                return False

    def register(self) -> None:
        self.username = str(input('Type your username: '))
        self.password = str(input('Type your password: '))
        login_check = self.__exists_user()
        if not login_check:
            with open('login.txt', 'ab') as f:
                s = repr([self.username, self.password])
                buff = base64.b64encode(s.encode('ascii'))
                f.write(buff)
                f.write('\n'.encode('ascii'))
            print('Your user has been registred.')
        else:
            print('This username cannot be used.')

    def login(self) -> bool:
        self.username = str(input('Type your username: '))
        self.password = str(input('Type your password: '))
        logon = self.__exists_user()
        with open('login.txt', 'rb') as f:
            all_logins = f.readlines()
            if logon:
                for login in all_logins:
                    current_login = base64.b64decode(login).decode('ascii')
                    current_login = ast.literal_eval(current_login)
                    if (self.username == current_login[self.USER_POS] and self.password == current_login[self.PASS_POS]):
                        print('Success!')
                        return True
        print('You password/username is not right.')

    def check_login(self) -> str:
        with open('login.txt', 'rb') as f:
            all_logins = f.readlines()
            logon = self.__exists_user()
            if logon:
                for index, login in enumerate(all_logins):
                    current_login = base64.b64decode(login).decode('ascii')
                    current_login = ast.literal_eval(current_login)
                    if (self.username == current_login[self.USER_POS] and self.password == current_login[self.PASS_POS]):
                        return str(self.username)

    def save_history(self) -> None:
        current_login = self.check_login()
        state = repr({'user': current_login, 'cart': self.cart})
        file_path = f'cart_{current_login}_{datetime.now().strftime("%Y_%m_%d")}.txt'
        with open(file_path, 'wb') as f:
            state = base64.b64encode(state.encode('ascii'))
            f.write(state)
            f.write('\n'.encode('ascii'))


def main() -> None:
    user = User()
    while True:
        opt = user.login_display()
        if (opt == 1):
            user.register()
        elif (opt == 2):
            logon = user.login()
            if logon:
                break
        else:
            quit()

    while True:
        ShoppingCart.welcome(user.username)
        try:
            option = int(input('Please enter an action: '))
            if (option == 1):
                user.cart.add_item()
            elif (option == 2):
                user.cart.view_cart()
            elif (option == 3):
                user.cart.remove_item()
            elif (option == 4):
                print(f'The total price of the items in the shopping cart is ${user.cart.total:.2f}')
            elif (option == 5):
                user.save_history()
                user.cart.quit()
                break
        except Exception as e:
            print('Something is wrong!\n', e)
            continue


if (__name__ == '__main__'):
    main()
