m1=float(input("enter the marks of CA out of 100\n"))
m2=float(input("enter the marks of MTE out of 40\n"))
m3=float(input("enter the marks of END Term out of 70\n"))
m4=float(input("enter the marks of Attendence out of 5\n"))
total=((m1*25/100)+(m2*20/40)+(m3*50/70)+m4)
cgpa=total/10
print("percentage is",total)
print("cgpa is",cgpa)
