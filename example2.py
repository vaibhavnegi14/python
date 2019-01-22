reading=int(input("enter the reading of electricity\n"))
if reading>100 :
  temp=reading-100
  extra=temp*6.95
  result=100*5.95+extra
else :
  result=reading*5.95
print("cost of electricity",result)
