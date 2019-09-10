"""
@author: Akhmad Kurbanov

The program is calculating how long it will take the user to 
save enough money to pay the down payment, while the salary is 
increasing every 6 months.
"""

# getting values form the user
annual_salary = float(input("Enter your annual salary: "))      
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

# predifined values
portion_down_payment = 0.25
current_savings = 0
r = 0.04 # annual rate
number_of_months = 0 

# calculating current savings until it hits down payment while 
# increasing annual salary each 6 months 
while current_savings < total_cost*portion_down_payment:
    if (number_of_months % 6 == 0) and (number_of_months != 0): 
        annual_salary += annual_salary*semi_annual_raise

    monthly_salary = annual_salary/12
    current_savings += current_savings*r/12 + portion_saved*monthly_salary
    number_of_months += 1 

print("Number of months:", number_of_months)
