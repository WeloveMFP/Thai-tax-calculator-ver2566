print("Hello welcome to tax calcu ver 2566")
all_income = int(input("Please input your yearly income:"))
wife = int(input("Do you have a lawful wife? Press 1 for yes, 0 for no:"))
del_wife = 60000 if wife == 1 else 0
children = int(input("Number of children under 20 years old:"))
del_children = children * 30000
birth = int(input("Spent on prenatal care and delivery cost in this year:"))
del_birth = min(birth, 60000)
parent = int(input("Number of alive parents (including wife's parents):"))
del_parent = parent * 30000
disable = int(input("Are you disabled? Press 1 for yes, 0 for no:"))
del_disable = 60000 if disable == 1 else 0
social_sec = int(input("Spent on social security in this year:"))
del_socialsec = min(social_sec, 6300)
house_interest = int(input("Yearly interest on housing purchases:"))
del_house = min(house_interest, 100000)
life_insurance = int(input("Yearly life insurance:"))
del_life_insurance = min(life_insurance, 100000)
health_insurance = int(input("Yearly health insurance:"))
del_health_insurance = min(health_insurance, 25000)
parent_insurance = int(input("Parent's yearly health insurance:"))
del_parent_insurance = min(parent_insurance, 15000)
pension_insurance = int(input("Yearly pension life insurance:"))
del_pension_insurance = min(pension_insurance, 200000)
national_saving_fund = int(input("Yearly National Saving Fund:"))
del_national_saving_fund = min(national_saving_fund, 13200)
provident_fund = int(input("Spent on provident fund in this year (without employer):"))
cal_provident_fund = min(provident_fund, all_income * 15 / 100)
gov_pension_fund = int(input("Yearly Government Pension Fund:"))
cal_gov_pension_fund = min(gov_pension_fund, all_income * 15 / 100)
private_teacher_aid_fund = int(input("Yearly private teacher aid fund:"))
cal_private_teacher_aid_fund = min(private_teacher_aid_fund, all_income * 15 / 100)
cal_500k = min(cal_provident_fund + cal_gov_pension_fund + cal_private_teacher_aid_fund, 500000)
rmf = int(input("Yearly RMF:"))
cal_RMF = min(rmf, all_income * 3 / 10)
del_RMF = min(cal_RMF, 500000)
ssf = int(input("Yearly SSF:"))
cal_SSF = min(ssf, all_income * 3 / 10)
del_SSF = min(cal_SSF, 200000)
cal_income = ((((((((((((((((all_income - 60000) - del_wife) - del_children) - del_birth) - del_parent) - del_disable) - del_house) - del_life_insurance) - del_health_insurance) - del_parent_insurance) - del_pension_insurance) - del_national_saving_fund) - del_500k) - del_RMF) - del_SSF) - del_socialsec)
donate = int(input("Donated in this year:"))
cal_donate = min(donate, cal_income * 1 / 10)
political_donate = int(input("Donated to any Thai political party in this year:"))
cal_political_donate = min(political_donate, 10000)
sum_income = cal_income - cal_donate - cal_political_donate
tax_thresholds = [0, 150000, 300000, 500000, 750000, 1000000, 2000000, 5000000, 18446744073709551615]
tax_rates = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
tax = 0
remaining_income = sum_income
for i in range(1, len(tax_thresholds)):
    if remaining_income <= 0:
        break
    taxable_amount = min(remaining_income, tax_thresholds[i] - tax_thresholds[i - 1])
    tax += taxable_amount * tax_rates[i - 1]
    remaining_income -= taxable_amount
print(f"Your estimated personal income tax for 2023 is: {tax:.2f} THB")
