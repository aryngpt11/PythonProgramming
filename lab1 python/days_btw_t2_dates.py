 #Python program to calculate no of days btw two dates

from datetime import date
d0 = date(2018,8,18)
d1 = date(2019,8,18)
delta = d1 - d0
print(delta.days)
