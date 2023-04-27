# MADE BY GABRRIEL CHAGAS BOFF

from datetime import datetime

def tax_calculator(subtotal, tax_rate):
    return round(((subtotal * tax_rate)/100), 2)

def total_calculator(tax, price):
    return round((tax + price), 2)

def subtotal_calculator(child_meal, adult_meal, qt_children, qt_adults):
    c = child_meal * qt_children
    a = adult_meal * qt_adults
    return round((c + a), 2)

def change_calculator(total, amount):
    return round((amount - total), 2)

def save_logs(values: str):
    with open('history_logs.txt', 'w') as f:
        f.write(values)

def main():
    
    child_meal = float(input('What is the price of a child\'s meal? '))
    adult_meal = float(input('What is the price of an adult\'s meal? '))
    qt_children = int(input('How many children are there? '))
    qt_adults = int(input('How many adults are there? '))
    tax_rate = float(input('What is the sales tax rate? '))
    subtotal = subtotal_calculator(child_meal, adult_meal, qt_children, qt_adults)
    sales_tax = tax_calculator(subtotal, tax_rate)
    total = total_calculator(sales_tax, subtotal)
    print(f"""\n
----------------------------------------
            
    Subtotal: ${subtotal}
    Sales Tax: ${sales_tax}
    Total: ${total}    
    
----------------------------------------    
    """)
    amount = float(input('\nWhat is the payment amount? '))
    change = change_calculator(total, amount)
    if (total > amount):
        print(f'\nInsuficient money! You need to pay more {abs(change)}')
    else:
        print(f'\nChange: ${change}')

    print('Thank you !')
    
    log = f"""\n
    Date: {datetime.now()}
    Subtotal: ${subtotal}
    Sales Tax: ${sales_tax}
    Total: ${total}
    Change: ${change}    
    """
    save_logs(log)

main()