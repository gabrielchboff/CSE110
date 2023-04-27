"""
Assignment
Write a program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.

To convert degrees in Fahrenheit to Celsius you need to subtract 32 from the Fahrenheit amount and then multiply it by the fraction 5/9.

Here is an example of the program when it runs:


What is the temperature in Fahrenheit? 81
The temperature in Celsius is 27.2 degrees.
Another example is:


What is the temperature in Fahrenheit? 12
The temperature in Celsius is -11.1 degrees.
"""
f = int(input('What is the temperature in Fahrenheit? '))
c = (f-32)*5/9
print(f'The temperature in Celsius is {c:.1f} degrees.')