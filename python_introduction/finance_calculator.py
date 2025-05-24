#defining variables
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

#formulas
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#results
print(f"Enter your monthly income: {monthly_income}")
print(f"Enter your total monthly expenses: {monthly_expenses}")
print(f"Your monthly savings are: {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {projected_savings}")