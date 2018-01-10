#!/usr/bin/env python3
from datetime import datetime
from dateutil.relativedelta import relativedelta


#diff. in second(s) and month(s)
d1 = datetime.today()
d2 = d1 + relativedelta(seconds=6)
d2 = d2 + relativedelta(minutes=1)
diff1 = relativedelta(d1, d2)
diff2 = relativedelta(d2, d1)
print(d1)
print(d2)
print(diff1.seconds)
print(diff2.seconds)
print((d2-d1).total_seconds())

#simple datetime calculator
d = datetime.strptime('2017-01-04', '%Y-%m-%d')
d = d + relativedelta(months=2, days=27)
print(d)

#datetime from string  ref. https://stackoverflow.com/a/466376/248616
d = datetime.strptime('2017-12', '%Y-%m')
print(d)
d = datetime.strptime('2017-12-26', '%Y-%m-%d')
print(d)

#add/minus month(s) to datetime
d2 = d - relativedelta(months=3)
print(d2)

#diff. in month(s)
d3 = datetime.today()
d4 = d3 - relativedelta(months=6)
diff  = relativedelta(d3, d4)
diff2 = relativedelta(d4, d3)
print(diff.months)
print(diff2.months)

d5 = datetime.today()
d6 = d5 + relativedelta(months=3, days=1) ;  diff = relativedelta(d6, d5) ; print(d5) ; print(d6) ; print(diff.months, diff.days)
d6 = d5 + relativedelta(months=2, days=31) ; diff = relativedelta(d6, d5) ; print(d5) ; print(d6) ; print(diff.months, diff.days)
d6 = d5 + relativedelta(months=2, days=30) ; diff = relativedelta(d6, d5) ; print(d5) ; print(d6) ; print(diff.months, diff.days)
d6 = d5 + relativedelta(months=2, days=29) ; diff = relativedelta(d6, d5) ; print(d5) ; print(d6) ; print(diff.months, diff.days)
d6 = d5 + relativedelta(months=2, days=28) ; diff = relativedelta(d6, d5) ; print(d5) ; print(d6) ; print(diff.months, diff.days)
d6 = d5 + relativedelta(months=2, days=27) ; diff = relativedelta(d6, d5) ; print(d5) ; print(d6) ; print(diff.months, diff.days)

#get end of month
d7 = datetime.today()
endingMonthDate = datetime(d7.year, d7.month, 1) \
                  + relativedelta(months=1) \
                  - relativedelta(days=1)
print(d7)
print(endingMonthDate)

