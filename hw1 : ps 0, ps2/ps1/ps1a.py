"""
@author: Akhmad Kurbanov

The program is calculating how long it will take the user to 
save enough money to pay the down payment.
"""

# getting values form the user
annual_salary = float(input("Enter your annual salary: "))      
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# predifined values
portion_down_payment = 0.25
current_savings = 0
monthly_salary = annual_salary/12
r = 0.04 #annual rate 
number_of_months = 0 
down_paymeny = total_cost*portion_down_payment

# calculating current savings until it hits down payment
while current_savings < down_paymeny:
    current_savings += current_savings*r/12 + portion_saved*monthly_salary
    number_of_months += 1 

print("Number of months:", number_of_months)
