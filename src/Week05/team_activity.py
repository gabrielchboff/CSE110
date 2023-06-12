print('Enter a list of numbers, type 0 when finished.\n')
numbers = []
while True:
    n = int(input('Enter number: '))
    if n == 0:
        break
    numbers.append(n)

list_sum = sum(numbers)
average = list_sum / len(numbers)
largest_number = sorted(numbers)[-1]
smallest = sorted(numbers)[0]

print(f"""
The sum is: {list_sum}
The average is: {average}
The largest number is: {largest_number}
The smallest number is: {smallest}
The smallest positive number is: {min([i for i in numbers if i > 0])}
The sorted list is:
""")

for number in sorted(numbers):
    print(number)
