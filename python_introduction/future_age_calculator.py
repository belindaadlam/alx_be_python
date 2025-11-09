# future_age_calculator.py

# Prompt the user for their current age. The input is converted to an integer
# immediately so we can perform calculations.
current_age = int(input("How old are you? "))

# Define the number of years between the current assumed year (2023) and 2050
YEARS_TO_ADD = 27

# Calculate the age the user will be in 2050
future_age = current_age + YEARS_TO_ADD

# Print the final result in the required format
print(f"In 2050, you will be {future_age} years old.")