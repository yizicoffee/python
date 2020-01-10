#DayDayUp.py
dayup=pow(1.01, 365)
dayback=pow(0.99, 365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup, dayback))

#DayDayUp1.py
dayfactor1 = 0.001
dayup1 = pow(1+dayfactor1, 365)
daydown1 = pow(1-dayfactor1, 365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup1,daydown1))

#DayDayUp2.py
dayup2=1
dayfactor2 = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup2 = dayup2*(1-dayfactor2)
    else:
        dayup2 = dayup2 * (1 + dayfactor2)
print("工作日向上：{:.2f}".format(dayup2))

#DayDayUp3.py
def dayUP(df):
    dayup3 = 1
    for i3 in range(365):
        if i3 % 7 in [6, 0]:
            dayup3 = dayup3 * (1 - 0.01)
        else:
            dayup3 = dayup3 * (1 + df)
    return dayup3
dayfactor3 = 0.01
while dayUP(dayfactor3) < 37.78:
    dayfactor3 += 0.001
print("{:.3f}".format(dayfactor3))
