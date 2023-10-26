# Define tax rates and deduction limits for 2023
tax_rates = {
    (0, 150000): 0.05,
    (150001, 500000): 0.1,
    (500001, 1000000): 0.2,
    (1000001, float('inf')): 0.35  # Use 'inf' for "and above"
}

# Initialize variables
income = float(input("Please input your yearly income: "))
total_deductions = 0

# Define deduction categories and ask for user input
deduction_categories = {
    "Marital Status": {
        "Lawful Wife": 60000,
    },
    "Children": {
        "Number of Children (under 20 years old)": 0,
    },
    "Medical Expenses": {
        "Prenatal Care and Delivery Cost": 0,
        "Parental Health Insurance": 0,
    },
    "Disability": {
        "Disability Status (1 for yes, 0 for no)": 0,
    },
    "Investments and Savings": {
        "Provident Fund": 0,
        "Social Security Contributions": 0,
        "RMF (Retirement Mutual Fund)": 0,
        "SSF (Super Savings Fund)": 0,
    },
    "Housing": {
        "Housing Interest": 0,
    },
    "Insurance": {
        "Life Insurance": 0,
        "Health Insurance": 0,
        "Parental Health Insurance": 0,
        "Pension Life Insurance": 0,
    },
    "Donations": {
        "General Donations": 0,
        "Political Party Donations": 0,
    }
}

# Loop through deduction categories and calculate deductions
for category, items in deduction_categories.items():
    print(f"Enter {category}:")
    for item, limit in items.items():
        deduction = float(input(f"How much did you spend on {item} in this year: "))
        deduction = min(deduction, limit)
        total_deductions += deduction

# Calculate taxable income
taxable_income = max(0, income - total_deductions)

# Calculate tax based on tax rates for the given income
tax_amount = 0
for income_range, rate in tax_rates.items():
    range_start, range_end = income_range
    if taxable_income > range_start:
        if range_end == float('inf'):
            taxable_range = taxable_income - range_start
        else:
            taxable_range = min(taxable_income, range_end) - range_start
        tax_amount += taxable_range * rate

# Print the results
print(f"Total Deductions: {total_deductions}")
print(f"Taxable Income: {taxable_income}")
print(f"Tax Amount: {tax_amount}")
