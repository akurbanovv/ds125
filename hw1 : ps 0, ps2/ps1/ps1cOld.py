
# all the calculations and logic are similar to the part A, but 
# in part B user's salary is increasing every 6 months. 

annual_salary = float(input("Enter the starting salary: "))      



# best_savings_rate = 0
bisection_steps = 0
# months_guess = 0

semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000


number_of_months = 36

lo = 0
hi = 10000



# IF ITS NOT POSSIBLE
# It is not possible to pay the down payment in three years.
# ELSE: 
while True:
    
    mid = (hi+lo)/2
    best_savings_rate = mid/10000 
    
    
    current_savings = 0 
    months_guess = 0
    while current_savings < total_cost*portion_down_payment:
        if (number_of_months % 6 == 0) and (number_of_months != 0): 
            annual_salary += annual_salary*semi_annual_raise
        monthly_salary = annual_salary/12
        current_savings += current_savings*r/12 + best_savings_rate*monthly_salary
        
        months_guess += 1

    
    if months_guess < number_of_months:
        print("ifbefore", hi)
        hi = mid
        print("if", hi)
    elif months_guess > number_of_months:
        lo = mid 
    else:
        print("Best savings rate:", best_savings_rate)
        print("Steps in bisection search:", bisection_steps)
        # break

    



    






    
  


         










print("Number of months:", best_savings_rate)



