# finance_calculator.py

# 1. Get User Input and convert to float
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# 2. Define the interest rate
ANNUAL_INTEREST_RATE = 0.05

# 3. Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# 4. Project Annual Savings
# (Monthly Savings * 12) * (1 + 0.05)
annual_savings_base = monthly_savings * 12
projected_savings = annual_savings_base * (1 + ANNUAL_INTEREST_RATE)

# 5. Output Results (using :.2f for currency formatting)
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")