total_bill = float(input('What is the total bill? '))
tip_percentage = int(input('What perecentage of the bill would you like to give as a tip? 10, 12 0r 15? '))
number_of_individuals = int(input('How many people are splitting the bill? '))

total_bill_and_tip = total_bill+(total_bill * tip_percentage/100)
bill_per_person = total_bill_and_tip/number_of_individuals
print(f'Each of you will have to pay: #{round(bill_per_person,2)}')
