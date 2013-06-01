# euler 19

from datetime import date
from datetime import timedelta


now = date(2005,5,26)
delta = timedelta(days=1)
print now
print now + delta
print now.weekday()
print (now + delta).weekday()

otherd = date(2005,5,26)
print(otherd == now)
print((now + delta) > otherd)

stop_date = date(2000,12,31)
now = date(1901,1,1)
no_sundays = 0
while True:
	if now.day == 1 and now.weekday() == 6:
		no_sundays += 1
	now += timedelta(days=1)
	if now > stop_date:
		break
print('number of sundays first in month: ', no_sundays)