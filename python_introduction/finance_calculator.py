monthly_income = int(input("What is your monthly income"))
monthly_expences = int(input("Enter yout total monthly expenses"))
monthly_savings = monthly_income - monthly_expences
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is:", projected_savings)
