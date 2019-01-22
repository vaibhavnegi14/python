ta=1000
ha=1000
gs=float(input("enter gross salary\n"))
wd=float(input("enter number of working days\n"))
total=gs+ta+ha
print("gross salary",total)
total1=(gs+ta+ha)%10
total2=total-total1
print("salary for 31 days",total2)
salary1=total2/31
print("salary for 1 day",salary1)
salary2=total2*wd/31
print("salary for ",wd,"days",salary2)

