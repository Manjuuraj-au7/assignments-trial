# Question No 3

sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))

avg=(sub1+sub2+sub3+sub4+sub5)/5

print (avg)

if (avg>90):
  print ('Grade A')
elif (avg>=70 and avg<90):
  print('Grade B')
elif (avg>=50 and avg<70):
  print('Grade C')
elif (avg>=30 and avg<50):
  print('Grade D')
elif (avg<30):
  print('Grade E')