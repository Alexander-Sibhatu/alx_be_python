total_monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_saving = int(total_monthly_income - total_monthly_expenses)

savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

print("Your monthly savings are", monthly_saving)
print("Projected savings after one year, with interest, is: ", savings)

