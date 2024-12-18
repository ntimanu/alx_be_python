monthly_income = float(input("What is your monthly income: "))
monthly_expences = float(input("Enter yout total monthly expenses: "))
monthly_savings = monthly_income - monthly_expences
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
