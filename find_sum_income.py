print("Hello welcome to tax calcu ver 2566")
all_income=int(input("Please input your yearly income :"))

#ลดหย่อนเมีย
wife = int(input("Do you have lawful wife? If you have, press 1. If you don't have, press 0 :"))
if wife == 1 :
    del_wife = 60000
else:
    del_wife=0

#ลดหย่อนลูก
children = int(input("How many children do you have (under 20 years old):"))
del_children = children*30000

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

#ลดกองทุนเลี้ยงชีพ (ไม่เกิน 500k)
provident_fund = int(input("How much did you spent provident fund in this year (without from employer) :"))
if provident_fund >= all_income*15/100:
    cal_provident_fund = all_income*15/100
else:
    cal_provident_fund = provident_fund

#ลดประกันสังคม
social_sec = int(input("How much did you spent social security in this year :"))
if social_sec >= 6300:
    del_socialsec = 6300
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

#คำนวณประกันชีวิต/สุขภาพ
cal_insurance = cal_life_insurance + cal_health_insurance
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

#ลดประกันชีวิตบำนาญ
pension_insurance = int(input("How much is your yearly pension life insurance :"))
if del_insurance == 0 :
    cal_pension_insurance = all_income*15/100
    if cal_pension_insurance >= 300000:
        del_pension_insurance = 300000
    else:
        del_pension_insurance = cal_pension_insurance
else:
    cal_pension_insurance = all_income*15/100
    if cal_pension_insurance >= 200000:
        del_pension_insurance = 200000
    else:
        del_pension_insurance = cal_pension_insurance

#ลดกองทุนบำเหน็จบำนาญข้าราชการ (ไม่เกิน 500k)
gov_pension_fund = int(input("How much is your yearly Government Pension Fund :"))
if gov_pension_fund>=all_income*15/100:
    cal_gov_pension_fund= all_income*15/100
else:
    cal_gov_pension_fund = gov_pension_fund

#ลดกองทุนออมแห่งชาติ 
national_saving_fund = int(input("How much is your yearly National Saving Fund :"))
if national_saving_fund>=13200:
    del_national_saving_fund= 13200
else:
    del_national_saving_fund = national_saving_fund

#ลดกองทุนครูเอกชน(ไม่เกิน 500k)
private_teacher_aid_fund = int(input("How much is your yearly private teacher aid fund :"))
if private_teacher_aid_fund >= all_income*15/100:
    cal_private_teacher_aid_fund = all_income*15/100
else:
    cal_private_teacher_aid_fund = private_teacher_aid_fund

#ลดไม่เกิน 500K
cal_500k = cal_provident_fund + cal_gov_pension_fund + cal_private_teacher_aid_fund
if cal_500k >= 500000:
    del_500k = 500000
else:
    del_500k = cal_500k

#ลด RMF
rmf = int(input("How much is your yearly RMF :"))
if rmf >= all_income*3/10:
    cal_RMF = all_income*3/10
else:
    cal_RMF = rmf
if cal_RMF >= 500000:
    del_RMF = 500000
else:
    del_RMF = cal_RMF

#ลด SSF
ssf = int(input("How much is your yearly SSF :"))
if ssf >= all_income*3/10:
    cal_SSF = all_income*3/10
else:
    cal_SSF = ssf
if cal_SSF >= 200000:
    del_SSF = 200000
else:
    del_SSF = cal_SSF

#คำนวณเงินได้หลังลดหย่อน
cal_income = all_income - 60000 - del_wife - del_children - del_birth - del_parent - del_disable - del_house - del_insurance - del_parent_insurance - del_pension_insurance - del_national_saving_fund - del_500k - del_RMF - del_SSF - del_socialsec

#ลดบริจาคทั่วไป
donate = int(input("How much did you donated in this year :"))
if donate >= cal_income*1/10:
    cal_donate = cal_income*1/10
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
print(sum_income)