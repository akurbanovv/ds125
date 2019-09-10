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
        print("00000000000000000")
        lo = mid 
    else:
        print("Best savings rate:", best_savings_rate)
        print("Steps in bisection search:", bisection_steps)
        # break