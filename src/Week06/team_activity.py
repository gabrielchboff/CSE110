TITLE = 2
NAME = 0
PID = 1
SALARY = 3

with open('hr_system.txt', 'r') as f:
    lines = f.readlines()
    persons = [line.split() for line in lines]

for person in persons:
    print(f'Name: {person[NAME].strip()}, Title: {person[TITLE].strip()}')

for person in persons:
    salary = float(person[SALARY])
    salary = salary / 24
    if person[TITLE].lower() == 'engineer':
        salary += 1000
    print(f'{person[NAME]} (ID: {person[PID]}), {person[TITLE]} - ${salary:.2f}')
