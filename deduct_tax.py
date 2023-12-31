#first 
print("Hello welcome to CRU SMART tax calculator ver 2566")
all_income=int(input("Please input your monthly income :"))
all_income*=12
all_income+=int(input("Please input your bonus this year :"))

#ลดหย่อนเมีย
wife = int(input("Do you have lawful wife? If you have, press 1. If you don't have, press 0 :"))
if wife == 1 :
    del_wife = 60000
else:
    del_wife = 0

# #ลดหย่อนลูก
children = int(input("How many children do you have (under 20 years old):"))
if children > 0:
 if children >= 2:
     cal_children = (children-1)*60000
 else:
     cal_children=0
 del_children = 30000+cal_children
else:
     del_children = 0

#ลดหย่อนค่าฝากครรภ์และทำคลอด
birth = int(input("How much did you spent on prenatal care and delivery cost in this year :"))
if birth >= 60000 :
     del_birth = 60000
else: 
     del_birth = birth

#ลดหย่อนพ่อแม่
parent = int(input("How many alive parent do you have (include your lawful wife's parents) :"))
del_parent = parent*30000

#ลดหย่อนพิการ
disable = int(input("Are you disable ? If yes, press 1. If no , press 0 :"))
if disable == 1: 
     del_disable = 60000
else:
     del_disable = 0

#ลดประกันสังคม
social_sec = int(input("How much did you spent social security in this year :"))
if social_sec >= 9000:
     del_socialsec = 9000
else :
     del_socialsec = social_sec

#ลดดอกบ้าน
house_interest = int(input("How much is your yearly interest on housing purchases :"))
if house_interest >= 100000:
     del_house = 100000
else:
     del_house = house_interest

#ลดประกันชีวิต
life_insurance = int(input("How much is your yearly life insurance :"))
if life_insurance >= 100000:
     cal_life_insurance = 100000
else:
     cal_life_insurance = life_insurance

#ลดประกันสุขภาพ
health_insurance = int(input("How much is your yearly health insurance :"))
if health_insurance >= 25000:
     cal_health_insurance = 25000
else:
     cal_health_insurance = health_insurance

#ประกันไม่เกิน 100k
cal_insurance = cal_life_insurance+cal_health_insurance
if cal_insurance >= 100000:
     del_insurance = 100000
else:
     del_insurance = cal_insurance

#ลดประกันพ่อแม่
parent_insurance = int(input("How much is your parent's yearly health insurance :"))
if parent_insurance >= 15000:
      del_parent_insurance = 15000
else:
      del_parent_insurance = parent_insurance

#ลดลงทุน social enterprise
social_enterprise = int(input("How much did you invest in social enterprise in this year :"))
if social_enterprise >= 100000:
     del_socialenterprise = 100000
else :
     del_socialenterprise = social_enterprise

#ลดกองทุนไทยเพื่อความยั่งยืน
Thai_ESG = int(input("How much is your yearly Thai ESG :"))
if Thai_ESG >=all_income*3/10:
      cal_thai_esg= all_income*3/10
else:
      cal_thai_esg = Thai_ESG
if cal_thai_esg >= 100000:
     del_thai_esg = 100000
else:
     del_thai_esg = cal_thai_esg

#ลดประกันชีวิตบำนาญ (ไม่เกิน 500k)
pension_insurance = int(input("How much is your yearly pension life insurance :"))
if pension_insurance >= all_income*15/100:
      calx_pension_insurance = all_income*15/100
else:
      calx_pension_insurance = pension_insurance
if calx_pension_insurance >= 200000 :
     cal_pension_insurance = 200000
else:
     cal_pension_insurance = calx_pension_insurance

#ลดกองทุนออมแห่งชาติ (ไม่เกิน 500k)
national_saving_fund = int(input("How much is your yearly National Saving Fund :"))
if national_saving_fund>=30000:
      cal_national_saving_fund= 30000
else:
      cal_national_saving_fund = national_saving_fund

#ลดกองทุนเลี้ยงชีพ (ไม่เกิน 500k)
provident_fund = int(input("How much did you spent provident fund in this year (without from employer) :"))
if provident_fund >= all_income*15/100:
      calx_provident_fund = all_income*15/100
else:
      calx_provident_fund = provident_fund
if calx_provident_fund >= 500000:
      cal_provident_fund = 500000
else:
      cal_provident_fund = calx_provident_fund

#ลดกองทุนบำเหน็จบำนาญข้าราชการ (ไม่เกิน 500k)
gov_pension_fund = int(input("How much is your yearly Government Pension Fund :"))
if gov_pension_fund>=all_income*3/10:
      calx_gov_pension_fund= all_income*3/10
else:
      calx_gov_pension_fund = gov_pension_fund
if calx_gov_pension_fund >= 500000:
      cal_gov_pension_fund = 500000
else:
      cal_gov_pension_fund = calx_gov_pension_fund

#ลดกองทุนครูเอกชน(ไม่เกิน 500k)
private_teacher_aid_fund = int(input("How much is your yearly private teacher aid fund :"))
if private_teacher_aid_fund >= all_income*15/100:
      calx_private_teacher_aid_fund = all_income*15/100
else:
      calx_private_teacher_aid_fund = private_teacher_aid_fund
if calx_private_teacher_aid_fund >= 500000:
      cal_private_teacher_aid_fund = 500000
else:
      cal_private_teacher_aid_fund = calx_private_teacher_aid_fund

#ลด RMF (ไม่เกิน 500k)
rmf = int(input("How much is your yearly RMF :"))
if rmf >= all_income*3/10:
      cal_RMF = all_income*3/10
else:
      cal_RMF = rmf
if cal_RMF >= 500000:
      del_RMF = 500000
else:
      del_RMF = cal_RMF

#ลด SSF (ไม่เกิน 500k)
ssf = int(input("How much is your yearly SSF :"))
if ssf >= all_income*3/10:
      cal_SSF = all_income*3/10
else:
      cal_SSF = ssf
if cal_SSF >= 200000:
      del_SSF = 200000
else:
      del_SSF = cal_SSF

#ลดไม่เกิน 500K
cal_500k = cal_provident_fund + cal_gov_pension_fund + cal_private_teacher_aid_fund + cal_pension_insurance +cal_national_saving_fund + del_SSF + del_RMF
if cal_500k >= 500000:
      del_500k = 500000
else:
      del_500k = cal_500k

#คำนวณเงินได้หลังลดหย่อน
cal_income = (((((((((((((all_income - 60000 )- del_wife )- del_children )- del_birth )- del_parent )- del_disable )- del_house )- del_insurance)- del_parent_insurance )- del_500k )- del_socialsec) -del_socialenterprise) -del_thai_esg)

#ลดบริจาคทั่วไป
donate = int(input("How much did you donated in this year :"))
if donate >= cal_income * 1/10:
      cal_donate = cal_income * 1/10
else:
      cal_donate = donate

#บริจาคพรรค
political_donate = int(input("How much did you donated to any Thai political party in this year :"))
if political_donate >= 10000:
      cal_political_donate = 10000
else:
      cal_political_donate = political_donate

#หาเงินได้สุทธิ
sum_income = cal_income - cal_donate - cal_political_donate

#คำนวณภาษี

def calculate_personal_income_tax(sum_income):
    # Tax rate thresholds and rates for 2023 (Thai tax year)
    tax_thresholds = [0, 150000, 300000, 500000, 750000, 1000000, 2000000, 5000000, 18446744073709551615]
    tax_rates = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]

    # Calculate tax
    tax = 0
    remaining_income = sum_income

    for i in range(1, len(tax_thresholds)):
        if remaining_income <= 0:
            break

        taxable_amount = min(remaining_income, tax_thresholds[i] - tax_thresholds[i - 1])
        tax += taxable_amount * tax_rates[i - 1]
        remaining_income -= taxable_amount

    return tax

def main():
    
    tax = calculate_personal_income_tax(sum_income)
    print(f"Your estimated personal income tax for 2023 is: {tax:.2f} THB")

if __name__ == "__main__":
    main()