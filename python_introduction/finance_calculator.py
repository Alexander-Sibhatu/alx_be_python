total_monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = float(total_monthly_income - total_monthly_expenses)

savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are", monthly_savings)
print("Projected savings after one year, with interest, is: ", savings)

