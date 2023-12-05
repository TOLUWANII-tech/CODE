age = int(input('How old are you? '))
no_of_years_left = 90 - age
no_of_weeks_left = no_of_years_left*52
no_of_days_left = no_of_years_left*365
no_of_months_left = no_of_years_left*12

print(f'You have {no_of_days_left} days, {no_of_weeks_left} weeks, and {no_of_months_left} months left to live till you are 90.')