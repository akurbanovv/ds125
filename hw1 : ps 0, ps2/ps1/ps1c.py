"""
@author: Akhmad Kurbanov

The programm is doing opposite of what we did in part 
B with predefined values. We have 32 months and we have to get 
the right rate with which we will save our money to pay down 
payment.
"""

# getting value from the user
annual_salary = float(input("Enter the starting salary: "))

# initial value of variables 
best_savings_rate = 0
bisection_steps = 0
current_savings = 0

# predifined values
semi_annual_raise = 0.07
portion_down_payment = 0.25
total_cost = 1000000
r = 0.04 # annual rate
down_payment = portion_down_payment * total_cost
number_of_months = 36

# values for bisection search 
lo = 0
hi = 10000

# at first check if it is possible to pay the down payment 
if (annual_salary*3 < down_payment):
    print("It is not possible to pay the down payment in three years.")
else:
    while True:        
        bisection_steps += 1

        # resetting vars to their initial values for the each interation 
        salary = annual_salary
        current_savings = 0
        mid = int((hi+lo)/2)
        best_savings_rate = mid/10000.0

        # counting amount of savings for each rate 
        for x in range(36):
            if (x % 6 == 0) and (x != 0):
                salary += salary*semi_annual_raise
            monthly_salary = salary/12
            current_savings += current_savings*r/12 + best_savings_rate*monthly_salary

        # using bisection search we are finding the right rate 
        if (abs(current_savings - down_payment) <= 100):
            print("Best savings rate:", best_savings_rate)
            print("Steps in bisection search:", bisection_steps)
            break
        elif (current_savings < down_payment): # too small rate
            lo = mid
        elif (current_savings > down_payment): # too big rate
            hi = mid
