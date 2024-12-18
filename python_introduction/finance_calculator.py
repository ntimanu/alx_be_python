monthly_income = input("What is your monthly income")
monthly_expences = input("Enter yout total monthly expenses")
monthly_savings = monthly_income - monthly_expences
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is:", projected_savings)
