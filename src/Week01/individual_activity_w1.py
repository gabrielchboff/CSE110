print('Please enter the following information:\n')
first_name = str(input('First name: '))
last_name = str(input('Last name: '))
email_address = str(input('Email address: '))
phone = str(input('Phone number: '))
job_title = str(input('Job title: '))
id_number = str(input('ID Number: '))

hair_color = str(input("Hair color: "))
eye_color = str(input("Eye color: "))
month = str(input("Starting Month: "))
training = str(input("Completed some training? "))

print(f"""
The ID car is:
----------------------------------------------
{last_name.capitalize()}, {first_name.title()}
{job_title.title()}
ID: {id_number}

{email_address}
{phone}
Hair: {hair_color.title()}		Eyes: {eye_color.title()}
Month: {month.title()}		Traning: {training.title()}
----------------------------------------------
""")
