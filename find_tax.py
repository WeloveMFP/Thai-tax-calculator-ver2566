def calculate_personal_income_tax(income):
    # Tax rate thresholds and rates for 2023 (Thai tax year)
    tax_thresholds = [0, 150000, 300000, 500000, 750000, 1000000, 2000000, 5000000, 18446744073709551615]
    tax_rates = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]

    # Calculate tax
    tax = 0
    remaining_income = income

    for i in range(1, len(tax_thresholds)):
        if remaining_income <= 0:
            break

        taxable_amount = min(remaining_income, tax_thresholds[i] - tax_thresholds[i - 1])
        tax += taxable_amount * tax_rates[i - 1]
        remaining_income -= taxable_amount

    return tax

def main():
    print("Welcome to the Thai Tax Calculator for the 2023 tax year")
    income = float(input("Please input your yearly income (THB): "))

    tax = calculate_personal_income_tax(income)
    print(f"Your estimated personal income tax for 2023 is: {tax:.2f} THB")

if __name__ == "__main__":
    main()
