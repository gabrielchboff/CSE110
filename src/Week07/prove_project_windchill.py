
class WindChillCalculator:
    def __init__(self, temperature) -> None:
        self.temperature = temperature

    def windchill(self, wind_speed) -> float:
        return 35.74 + 0.6215 * self.temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * self.temperature * (wind_speed ** 0.16)
    
    def celcius_to_fahrenheit(self, temperature) -> float:
        return (temperature * 1.8) + 32

    def calculate(self, temp_format='F') -> None:
        for i in range(5, 60, 5):
            wind_speed = i
            if temp_format.capitalize() == 'C':
                current_temperature = self.celcius_to_fahrenheit(self.temperature)
                wind_chill = self.windchill(wind_speed)
                print(f'At temperature {current_temperature} °F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f} °F')
            else:
                wind_chill = self.windchill(wind_speed)
                print(f'At temperature {self.temperature} °F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f} °F')



class Menu:

    @staticmethod
    def print_menu():
        print("""
        ------------------------------------------------------------------

           PROGRAMMING PROJECT: WINDCHILL CALCULATOR

           CHOOSE AN OPTION:

           1. Calculate windchill by temperature and random wind speed
           2. Calculate windchill by temperature and fixed wind speed
           3. Exit

        ------------------------------------------------------------------
        """)

    @staticmethod
    def get_menu_choice():
        return int(input('Enter your choice: '))
    
    @staticmethod
    def calculate_random():
        temperature = float(input('What is the temperature? '))
        temp_format = str(input('Fahrenheit or Celsius (F/C)? '))
        wind_chill = WindChillCalculator(temperature)
        if temp_format.capitalize() == 'C':
            wind_chill.calculate(temp_format=temp_format)
        else:
            wind_chill.calculate()
        del wind_chill
    
    @staticmethod
    def calculate_fixed():
        temperature = float(input('What is the temperature (°F)? '))
        wind_speed = float(input('What is the wind speed (mph)? '))
        wind_chill = WindChillCalculator(temperature)
        windchill = wind_chill.windchill(wind_speed)
        print(f'At temperature {temperature} °F, and wind speed {wind_speed} mph, the windchill is: {windchill:.2f} °F')
        del wind_chill

def main():
    while True:
        Menu.print_menu()
        choice = Menu.get_menu_choice()
        if choice == 1:
            Menu.calculate_random()
        elif choice == 2:
            Menu.calculate_fixed()
        elif choice == 3:
            print('Exiting...')
            break


if __name__ == '__main__':
    main()