total_monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_saving = float(total_monthly_income) - float(total_monthly_expenses)

savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

print("Your monthly savings are", monthly_saving)
print("Projected savings after one year, with interest, is: ", savings)

